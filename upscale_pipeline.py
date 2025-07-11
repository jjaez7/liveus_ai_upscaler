from modules.transcribe_audio import transcribe_audio
from modules.translate_srt_with_gpt import translate_segments
from modules.segments_to_srt import save_srt
from modules.run_real_esrgan import run_esrgan
from modules.burn_subtitles import burn_srt
import sys
import os

def main():
    if len(sys.argv) < 4:
        print("Usage: python upscale_pipeline.py <input_video> <lang> <target_lang>")
        return

    input_path = sys.argv[1]
    lang = sys.argv[2]
    target_lang = sys.argv[3]

    print("1. Transcribing...")
    segments = transcribe_audio(input_path, lang)

    print("2. Translating...")
    translated = translate_segments(segments, lang, target_lang)

    print("3. Saving subtitles...")
    srt_path = input_path.replace('.mp4', '.srt')
    save_srt(translated, srt_path)

    print("4. Upscaling video...")
    upscaled_path = run_esrgan(input_path)

    print("5. Burning subtitles...")
    final_video = burn_srt(upscaled_path, srt_path)

    print("Done! Final video:", final_video)

if __name__ == "__main__":
    main()
