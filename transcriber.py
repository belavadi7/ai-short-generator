import whisper

def transcribe(video_path):
    model = whisper.load_model("base")
    result = model.transcribe(video_path)

    print("\n📝 Transcript Segments:")
    for i, seg in enumerate(result["segments"]):
        print(f"[{i}] {seg['start']}s - {seg['end']}s: {seg['text']}")

    return result["text"], result["segments"]
