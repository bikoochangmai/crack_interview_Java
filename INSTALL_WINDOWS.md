# Install V5 on Windows

1. Download the V5 ZIP in ChatGPT, press **Ctrl+J** in Edge, and choose **Show in folder**.
2. Back up or commit your repository changes before copying files.
3. Use the PowerShell file picker to locate the downloaded ZIP:

```powershell
Add-Type -AssemblyName System.Windows.Forms
$d = New-Object System.Windows.Forms.OpenFileDialog
$d.Filter = 'ZIP archives (*.zip)|*.zip'
if ($d.ShowDialog() -ne 'OK') { throw 'No archive selected' }
$zip = $d.FileName
$repo = 'D:\workspace\Learnings\JAVA_QUESTIONS\crack_interview_Java'
$temp = Join-Path $env:TEMP 'java_interview_v5_import'
Expand-Archive -LiteralPath $zip -DestinationPath $temp -Force
Get-ChildItem -LiteralPath $temp -Force | Copy-Item -Destination $repo -Recurse -Force
Set-Location $repo
py .\scripts\validate_questions.py
py .\scripts\validate_leetcode.py
git status
```

4. Review changes, then `git add .`, `git commit -m "Expand foundational study walkthroughs"`, and `git push origin main`.
