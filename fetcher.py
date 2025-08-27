import os
import yt_dlp
from concurrent.futures import ThreadPoolExecutor, as_completed

OUTPUT_DIR = "./downloads"

def download_single(url, output_path=OUTPUT_DIR):
    """Download a single video using yt-dlp"""
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,  # only one video at a time
        'quiet': True,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return f"✅ Downloaded: {info.get('title', 'Unknown Title')}"
    except Exception as e:
        return f"❌ Error downloading {url}: {e}"

def download_playlist_async(playlist_url, max_workers=4):
    """Download all videos in a playlist asynchronously"""
    with yt_dlp.YoutubeDL({'extract_flat': True, 'quiet': True}) as ydl:
        info = ydl.extract_info(playlist_url, download=False)
        if 'entries' not in info:
            print("Not a playlist. Downloading as a single video...")
            print(download_single(playlist_url))
            return

        title = info.get('title', 'Untitled Playlist')
        entries = info['entries']
        print(f"Found playlist: {title}")
        print(f"Total videos: {len(entries)}")

        # Create subfolder for playlist
        playlist_folder = os.path.join(OUTPUT_DIR, title.replace(" ", "_"))
        os.makedirs(playlist_folder, exist_ok=True)

        # Start parallel downloads
        urls = [entry['url'] for entry in entries if entry]
        results = []
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(download_single, url, playlist_folder): url for url in urls}
            for future in as_completed(futures):
                results.append(future.result())
                print(results[-1])  # log as they finish

        print("\n🎉 All downloads completed!")

if __name__ == "__main__":
    link = input("Enter YouTube video or playlist URL: ").strip()
    download_playlist_async(link, max_workers=4)