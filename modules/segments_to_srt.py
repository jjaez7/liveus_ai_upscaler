from datetime import timedelta

def format_time(seconds):
    td = timedelta(seconds=float(seconds))
    return str(td).split('.')[0].rjust(8, '0').replace('.', ',')

def save_srt(segments, path):
    with open(path, 'w', encoding='utf-8') as f:
        for i, seg in enumerate(segments):
            start = format_time(seg['start'])
            end = format_time(seg['end'])
            f.write(f"{i+1}\n")
            f.write(f"{start},000 --> {end},000\n")
            f.write(f"{seg['text']}\n\n")
