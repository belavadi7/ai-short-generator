from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

def create_shorts(video_path, segments, output_dir="shorts_output"):
    os.makedirs(output_dir, exist_ok=True)
    short_count = 0

    for i, segment in enumerate(segments):
        start = segment["start"]
        end = segment["end"]
        text = segment["text"].strip()

        # Skip segments that are too short or too long
        if len(text) < 5 or (end - start) > 60:
            continue

        try:
            clip = VideoFileClip(video_path).subclip(start, end)
            caption = TextClip(text, fontsize=24, color="white", bg_color="black").set_duration(clip.duration)
            final = CompositeVideoClip([clip, caption.set_position(("center", "bottom"))])

            output_path = os.path.join(output_dir, f"short_{i+1}.mp4")
            final.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=24)
            short_count += 1
        except Exception as e:
            print(f"⚠️ Skipped segment {i}: {e}")

    print(f"\n✅ Created {short_count} shorts.")
