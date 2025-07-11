# 🎤 LIVEUS AI Upscaler

> AI-Powered Subtitle + Translation + 4K Upscaling Pipeline for Concert Videos

LIVEUS AI Upscaler is an end-to-end Python pipeline that automates:
- Subtitle generation via Whisper
- Emotional translation using GPT-4
- 4K video enhancement with Real-ESRGAN
- Subtitles embedding using FFmpeg

This project originated from [LIVEUS](https://github.com/your-org/liveus), a K-POP concert streaming platform.

---

##  Why Use This?

Concert videos often:
- lack multilingual subtitles,
- are low-resolution,
- require manual post-production.

This pipeline automates everything using advanced AI.

---

##  Use Cases

- Subtitling K-POP concerts in multiple languages
- Emotion-preserving lyric translation
- Enhancing old 720p/1080p videos to 4K
- Embedding subtitles into MP4 for streaming or offline viewing
- Creating localized highlight reels

---

##  Example Output

| Original | Enhanced |
|----------|----------|
| `examples/input.mp4` | `examples/output.mp4` |

> `input.mp4`: A concert clip without subtitles  
> `output.mp4`: Translated, upscaled, and subtitle-burned final result

---

## 🛠️ Pipeline Overview

[input.mp4]
↓
[1. Whisper] → Japanese transcript (segments)
↓
[2. GPT-4] → Emotionally translated English
↓
[3. Real-ESRGAN] → 4K enhanced video
↓
[4. FFmpeg] → Subtitle burn-in


---

## 🖥️ Supported Platforms

- ✅ Windows 10/11
- ✅ macOS
- ✅ Ubuntu/Linux

---

## 📁 Folder Structure

liveus_ai_upscaler/
├── upscale_pipeline.py
├── requirements.txt
├── .env.example
├── modules/
│ ├── transcribe_audio.py
│ ├── translate_srt_with_gpt.py
│ ├── segments_to_srt.py
│ ├── run_real_esrgan.py
│ └── burn_subtitles.py
└── examples/
├── input.mp4
└── output.mp4


---

## 📦 Installation (Windows Guide)

### 1. Clone the repository

```bash
git clone https://github.com/yourname/liveus_ai_upscaler.git
cd liveus_ai_upscaler
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API Key
```bash
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

## 🎬 Running the Pipeline
```bash
python upscale_pipeline.py examples/input.mp4 ja en
```

- This will:
- Transcribe Korean audio
- Translate it to English using GPT-4
- Save .srt subtitles
- Enhance video to 4K with Real-ESRGAN
- Burn subtitles into final MP4

## OUTPUT:
```bash
examples/input.srt
examples/input_upscaled.mp4
examples/input_upscaled_final.mp4 → renamed to output.mp4
```
## Required Models
### 1. Whisper
```python
import whisper
model = whisper.load_model("medium")
```
### 2. GPT
- Signup: https://platform.openai.com
- Place key in .env

### 3. Real-ESRGAN
Download pretrained model manually:
```ruby
https://github.com/xinntao/Real-ESRGAN/releases/download/v0.2.5/RealESRGAN_x4plus.pth
```
place in
```bash
RealESRGAN/weights/RealESRGAN_x4plus.pth
```

### 4. FFmpeg
- Windows: https://ffmpeg.org/download.html
- Add ffmpeg.exe to system PATH

## Tips
You can change source/target language (ja → en, ko → en, etc.)
Whisper supports dozens of languages
GPT-4 handles song lyrics surprisingly well when prompted properly

## Ideas for Extensions
Streamlit drag & drop UI
Auto language detection
Add voice-to-voice dubbing with ElevenLabs
Batch processing support

## Contributing
Pull requests welcome! Especially for:
More language support
UX enhancements
GPU optimization
Lee Ju Won

## License
This project: MIT License
Whisper: Apache 2.0
Real-ESRGAN: BSD 3-Clause
GPT-4: OpenAI API (usage only)

## Acknowledgements
Whisper
OpenAI GPT-4
Real-ESRGAN
FFmpeg

Created with jjaez7