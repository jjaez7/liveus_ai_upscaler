import subprocess

def run_esrgan(input_path):
    output_path = input_path.replace('.mp4', '_upscaled.mp4')
    command = [
        "python", "RealESRGAN/inference_realesrgan.py",
        "-i", input_path,
        "-n", "RealESRGAN_x4plus",
        "-o", output_path
    ]
    subprocess.run(command, check=True)
    return output_path
