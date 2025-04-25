from pytubefix import Playlist, YouTube
#sorry for not commenting
import os
import re
from tqdm import tqdm

def sanitize_filename(name):
    """Remove invalid characters from folder/file names"""
    return re.sub(r'[\\/*?:"<>|]', '', name)

playlist_url = input("Enter YouTube Playlist URL: ")
playlist = Playlist(playlist_url)


playlist_title = sanitize_filename(playlist.title)
download_dir = os.path.join(os.getcwd(), playlist_title)
os.makedirs(download_dir, exist_ok=True)

print(f"Downloading: {playlist.title}")
print(f"Videos found: {len(playlist.videos)}")

for video in tqdm(playlist.videos, desc="Progress"):
    try:
        yt = YouTube(video.watch_url, 
                   use_oauth=True,
                   allow_oauth_cache=True)
        
        
        stream = yt.streams.get_highest_resolution()
        
        stream.download(output_path=download_dir)
        
    except Exception as e:
        print(f"\nError downloading {video.title}: {str(e)}")

print(f"\nDownload complete! Videos saved to: {download_dir}")
