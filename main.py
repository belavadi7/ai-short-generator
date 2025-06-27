from video_downloader import download_video
from transcriber import transcribe
from highlight_picker import find_highlights
from video_editor import create_shorts

def main():
    url = input("Enter YouTube URL: ").strip()
    video = download_video(url)
    print("Transcribing…")
    _, segments = transcribe(video)
    highlights = find_highlights(segments)
    print(f"Creating {len(highlights)} shorts…")
    clips = create_shorts(video, highlights)
    print("Done! Check the `shorts_output/` folder:")
    for c in clips:
        print("  -", c)

if __name__ == "__main__":
    main()
