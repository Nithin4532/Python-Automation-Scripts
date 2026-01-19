import os

# Folder path where files are present
folder_path = "files"

# Get list of files
files = os.listdir(folder_path)

# Rename files
for index, filename in enumerate(files):
    old_path = os.path.join(folder_path, filename)
    new_name = f"file_{index + 1}.txt"
    new_path = os.path.join(folder_path, new_name)

    os.rename(old_path, new_path)

print("Files renamed successfully!")
