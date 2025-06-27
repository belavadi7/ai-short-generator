def find_highlights(segments):
    keywords = ["wow", "amazing", "funny", "shocking"]
    return [s for s in segments if any(kw in s["text"].lower() for kw in keywords)][:3]
