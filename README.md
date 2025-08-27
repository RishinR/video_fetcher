# 🎶 Video Fetcher

A simple and lightweight **media utility tool** that lets you:

* Fetch and organize video/audio files.
* Play all songs in a folder seamlessly.
* Handle both single files and playlists.

## 🚀 Features

* Download and organize media into a folder structure.
* Automatically detect and play all `.mp4` songs in a given folder.
* Playlist support (plays files sequentially).
* Works cross-platform (Linux, macOS, Windows).
* Lightweight and async-ready for handling multiple files.

## 📂 Project Structure

```
video_fetcher/
│── fetcher.py     # Script to fetch and organize media files
│── player.py      # Simple media player for local .mp4 files
│── requirements.txt
│── README.md
```

## ⚡ Usage

### 1️⃣ Run the Fetcher

```bash
python fetcher.py
```

This will fetch and organize your media files into the desired folder.

### 2️⃣ Play All Songs in a Folder

```bash
python player.py
```

* The script will scan the folder.
* Collect all `.mp4` files.
* Play them one by one automatically.

---

## 🛠 Requirements

* Python 3.8+
* VLC installed (for playback)

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ✅ Future Enhancements

* Shuffle mode for playlists.
* Pause/Resume/Skip controls.
* Support for more file formats (`.mp3`, `.wav`, `.mkv`).

---

## 📜 License

This project is licensed under the MIT License – feel free to use, modify, and share.
