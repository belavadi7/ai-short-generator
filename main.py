from video_downloader import download_video
from transcriber import transcribe
from video_editor import create_shorts

def main():
    url = input("Enter YouTube URL: ")
    video = download_video(url)
    print("Transcribing…")
    _, segments = transcribe(video)
    print("Creating shorts…")
    create_shorts(video, segments)
    print("✅ Done! Check the `shorts_output/` folder.")

if __name__ == "__main__":
    main()
