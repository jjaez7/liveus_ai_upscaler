import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def translate_segments(segments, source_lang="ja", target_lang="en"):
    texts = [seg['text'] for seg in segments]
    prompt = f"Translate the following subtitles from {source_lang} to {target_lang}, preserving emotional meaning:\n\n"
    prompt += "\n".join(texts)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    translated = response.choices[0].message.content.strip().split("\n")
    for i, line in enumerate(translated):
        segments[i]['text'] = line
    return segments
