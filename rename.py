with open("renamed.txt") as f:
    content=f.read()
with open("renamed_by_ python.txt","w") as f:
    f.write(content)

import os

file_path = "renamed.txt"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist.")
