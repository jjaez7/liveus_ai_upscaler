import subprocess

def burn_srt(video_path, srt_path):
    output_path = video_path.replace('.mp4', '_final.mp4')
    command = [
        "ffmpeg", "-i", video_path,
        "-vf", f"subtitles='{srt_path}':force_style='FontName=Noto Sans,FontSize=24,PrimaryColour=&HFFFFFF&'",
        "-c:a", "copy",
        output_path
    ]
    subprocess.run(command, check=True)
    return output_path
