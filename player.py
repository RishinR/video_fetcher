import os
import subprocess

def play_all_mp4(folder="./downloads"):
    files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".mp4")]
    if not files:
        print("No .mp4 files found.")
        return

    print(f"Playing {len(files)} songs/videos in VLC...")
    subprocess.run(["/Applications/VLC.app/Contents/MacOS/VLC", "--play-and-exit"] + files)

if __name__ == "__main__":
    play_all_mp4("./downloads/<path_to_your_mp4_files_folder>")
