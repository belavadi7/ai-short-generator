import whisper

def transcribe(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    return result["text"], result["segments"]
