# video_downloader.py

import yt_dlp
import os
import re

def sanitize_filename(title):
    # Replace spaces and remove special characters
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', title)

def download_video(url, output_path="downloads"):
    os.makedirs(output_path, exist_ok=True)
    ydl_opts = {
        'format': 'mp4',
        'quiet': True,
        'outtmpl': f'{output_path}/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        original_title = info['title']
        original_path = os.path.join(output_path, f"{original_title}.mp4")
        safe_title = sanitize_filename(original_title)
        final_path = os.path.join(output_path, f"{safe_title}.mp4")
        os.rename(original_path, final_path)
        return final_path
