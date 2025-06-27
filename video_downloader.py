# video_downloader.py

import yt_dlp
import os
import re

def sanitize_filename(name):
    return re.sub(r'[^a-zA-Z0-9_\-]', '_', name)

def download_video(url, output_path="downloads"):
    os.makedirs(output_path, exist_ok=True)

    video_path = None

    def on_download_complete(d):
        nonlocal video_path
        if d['status'] == 'finished':
            video_path = d['filename']

    ydl_opts = {
        'format': 'mp4',
        'quiet': True,
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'progress_hooks': [on_download_complete],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)

    if not video_path:
        raise RuntimeError("Download failed or video path not captured")

    # Now sanitize it
    safe_name = sanitize_filename(os.path.basename(video_path))
    safe_path = os.path.join(output_path, safe_name)

    if video_path != safe_path:
        os.rename(video_path, safe_path)

    return safe_path
