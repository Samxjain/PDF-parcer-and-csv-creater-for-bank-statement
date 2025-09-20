import os
import shutil
from pathlib import Path

# Path to Downloads folder
DOWNLOADS = Path.home() / "Downloads"

# File type mapping (extension: folder name)
FILE_TYPES = {
    "pdf": "Docs",
    "jpg": "Images",
    "jpeg": "Images",
    "png": "Images",
    "gif": "Images",
    "zip": "Zips",
    "rar": "Zips",
    "7z": "Zips",
    "docx": "Docs",
    "doc": "Docs",
    "txt": "Text",
    "xlsx": "Spreadsheets",
    "csv": "Spreadsheets",
    "mp3": "Music",
    "mp4": "Videos",
    "mov": "Videos",
}

def organize_downloads():
    for file in DOWNLOADS.iterdir():
        if file.is_file():
            ext = file.suffix.lower().lstrip(".")
            if ext in FILE_TYPES:
                folder = DOWNLOADS / FILE_TYPES[ext]
                folder.mkdir(exist_ok=True)  # create subfolder if it doesn’t exist
                shutil.move(str(file), str(folder / file.name))
                print(f"Moved {file.name} → {folder}")
            else:
                # Optional: move unknown files into "Others"
                other_folder = DOWNLOADS / "Others"
                other_folder.mkdir(exist_ok=True)
                shutil.move(str(file), str(other_folder / file.name))
                print(f"Moved {file.name} → {other_folder}")

if __name__ == "__main__":
    organize_downloads()
