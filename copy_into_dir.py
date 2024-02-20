import os
import shutil

def copy_files(source_dir, target_dir):
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Construct the file path
            file_path = os.path.join(root, file)
            
            # Construct the destination path
            dest_path = os.path.join(target_dir, file)
            
            # Move the file
            shutil.copy(file_path, dest_path)
            print(f"Copied: {file_path} -> {dest_path}")
    

source_directory = input("Enter the path to the source directory: ")
target_directory = input("Enter the path to the target directory: ")

copy_files(source_directory, target_directory)
