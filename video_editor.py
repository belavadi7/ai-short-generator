from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

def create_shorts(video_path, highlights):
    os.makedirs("shorts_output", exist_ok=True)
    results = []
    for idx, seg in enumerate(highlights):
        clip = VideoFileClip(video_path).subclip(seg["start"], seg["end"])
        clip = clip.resize(height=1080)
        txt = TextClip(seg["text"], fontsize=36, color="white", bg_color="black", size=(clip.w, None))
        txt = txt.set_duration(clip.duration).set_position(("center", "bottom"))
        comp = CompositeVideoClip([clip, txt])
        out_path = f"shorts_output/short_{idx+1}.mp4"
        comp.write_videofile(out_path, codec="libx264")
        results.append(out_path)
    return results
