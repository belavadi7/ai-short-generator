# video_downloader.py

import yt_dlp
import os

def download_video(url, output_path="downloads"):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        return os.path.join(output_path, f"{info['title']}.mp4")
