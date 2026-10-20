param(
  [ValidateSet('Sample','All')][string]$Scope='Sample',
  [ValidateSet('Question','Both')][string]$Content='Both'
)
$ErrorActionPreference='Stop'
$root=Split-Path -Parent $PSScriptRoot
Set-Location $root
Add-Type -AssemblyName System.Speech
$engine=New-Object System.Speech.Synthesis.SpeechSynthesizer
$engine.Rate=-1
$questions=Get-Content '.\data\questions.json' -Raw | ConvertFrom-Json
$manifestPath=Join-Path $root 'audio\manifest.json'
if(Test-Path $manifestPath){$manifest=Get-Content $manifestPath -Raw | ConvertFrom-Json}else{$manifest=@{}}
# -AsHashtable requires PowerShell 7; support Windows PowerShell 5.1 too
if($manifest -isnot [System.Collections.IDictionary]){
 $old=$manifest;$manifest=@{};if($old){$old.PSObject.Properties|ForEach-Object{$manifest[$_.Name]=@{};foreach($p in $_.Value.PSObject.Properties){$manifest[$_.Name][$p.Name]=$p.Value}}}
}
$items=if($Scope -eq 'Sample'){$questions|Select-Object -First 3}else{$questions}
$ffmpeg=Get-Command ffmpeg -ErrorAction SilentlyContinue
foreach($q in $items){
 $id=[string]$q.id
 if(-not $manifest.ContainsKey($id)){$manifest[$id]=@{}}
 foreach($kind in @('question','explanation')){
  if($kind -eq 'explanation' -and $Content -ne 'Both'){continue}
  $text=if($kind -eq 'question'){$q.question}else{(@($q.explanation,$q.why,$q.example,$q.tradeoffs)|Where-Object{$_}) -join '. '}
  if([string]::IsNullOrWhiteSpace($text)){continue}
  $folder=Join-Path $root "audio\$kind";New-Item -ItemType Directory -Force -Path $folder|Out-Null
  $wav=Join-Path $folder "$id.wav";$mp3=Join-Path $folder "$id.mp3"
  Write-Host "Generating $kind for question $id"
  try{$engine.SetOutputToWaveFile($wav);$engine.Speak([string]$text)}finally{$engine.SetOutputToNull()}
  if($ffmpeg){& ffmpeg -nostdin -loglevel error -y -i $wav -codec:a libmp3lame -b:a 64k $mp3;if($LASTEXITCODE -ne 0){throw 'ffmpeg failed'};Remove-Item $wav; $manifest[$id][$kind]="audio/$kind/$id.mp3"}
  else{$manifest[$id][$kind]="audio/$kind/$id.wav"}
 }
 $manifest|ConvertTo-Json -Depth 5|Set-Content -Encoding utf8 $manifestPath
}
$engine.Dispose()
Write-Host "Finished. Generated audio assets and updated $manifestPath."
