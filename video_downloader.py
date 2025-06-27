from pytube import YouTube

def download_video(url, save_path="downloaded_video.mp4"):
    yt = YouTube(url)
    stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
    stream.download(filename=save_path)
    return save_path
