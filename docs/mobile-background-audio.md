# V6.6 — Mobile audio / locked-screen playback

The portal uses **HTML5 audio** for recorded files, with Media Session metadata and play/pause/next/previous handlers. Unlike browser speech synthesis, this is the correct web-media mechanism for background audio. **Lock-screen continuation is OS/browser-dependent and cannot be guaranteed**. Test Safari on iOS and Chrome on Android on real phones. Keep the browser tab open and start playback with a user tap.

## What's included

- Recorded MP3 samples for questions 1–3 (questions only), produced with an offline synthesized voice.
- `audio/manifest.json` links recorded audio to each question.
- `scripts/generate_mobile_audio.ps1` generates audio for all 314 questions and explanations on Windows using `System.Speech`.
- When an audio file is missing, the UI falls back to browser narration, **which is not reliable when the screen is locked**.

## Generate audio for every question (Windows)

In PowerShell, from the project root:

```powershell
& .\scripts\generate_mobile_audio.ps1 -Scope Sample -Content Both
# After confirming sample audio quality and storage needs:
& .\scripts\generate_mobile_audio.ps1 -Scope All -Content Both
```

The script writes WAV files using Windows speech voices. If `ffmpeg` is on PATH, it converts them to smaller MP3 files. Generation can take considerable time and produce a large amount of data; inspect the resulting `audio/` folder before committing to GitHub. GitHub has repository/file size and Pages usage constraints. You can choose `-Content Question` to generate shorter question-only audio.

After generation, validate paths with `py scripts/validate_audio_manifest.py`, then commit `audio/` and deploy. If you need a natural neural voice, use a separately configured TTS provider and regenerate the audio assets; no cloud provider is embedded or charged by this version.

## Testing

1. On desktop, expand Question #1, tap **Question**; a persistent player appears.
2. On Android Chrome and iOS Safari, tap Question #1, then lock the screen and listen. Try pause/resume from the lock screen or headphones.
3. Test automatic next question **only after** generating recordings for the selected category; browser TTS fallback cannot guarantee locked-screen playback.
4. Verify changing question filters does not interrupt a playing MP3.
5. Test with battery saver, Bluetooth headphones, silent mode, and different browsers.

No user data is uploaded by the audio player. Study progress remains in browser-local storage.
