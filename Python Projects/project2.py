import os
import shutil

source_folder = "C:/Users/HP/Downloads"

folder_map = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mov", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar", ".7z"],
    "Others": []  # fallback
}

def organize_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(filename)
            ext = ext.lower()

            moved = False
            for folder, extensions in folder_map.items():
                if ext in extensions:
                    dest_folder = os.path.join(folder_path, folder)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, filename))
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))

organize_folder(source_folder)
print("Organized successfully!")