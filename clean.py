import os
import glob

# Get the current working directory
current_directory = os.getcwd()

# Use glob to find all index.html files in the current directory and its subdirectories
for file_path in glob.glob(f'{current_directory}/**/index.html', recursive=True):
    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        # Delete the file
        os.remove(file_path)
        print(f'Deleted: {file_path}')