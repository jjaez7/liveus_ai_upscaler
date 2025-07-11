import whisper

def transcribe_audio(input_path, lang='ja'):
    """
    Transcribe audio from a video file using OpenAI Whisper.

    Args:
        input_path (str): Path to the input video file (e.g., .mp4).
        lang (str): Language code of the spoken language (e.g., 'ja', 'en').

    Returns:
        List[dict]: List of segments, each with 'start', 'end', and 'text'.
    """
    model = whisper.load_model("medium")  # or "large" if more accurate results are desired
    result = model.transcribe(input_path, language=lang)
    return result['segments']  # Each segment: {'start': float, 'end': float, 'text': str}
