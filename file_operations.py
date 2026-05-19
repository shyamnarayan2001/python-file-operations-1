import os
import shutil

# Define file paths
source_file = 'C:\\temp\\source.txt'
destination_file = 'C:\\temp\\destination.txt'
directory_path = 'C:\\temp\\my_directory'

# Create a source file
try:
    with open(source_file, 'w') as f:
        f.write('This is a source file.\n')
except Exception as e:
    print(f'Error creating source file: {e}')

# Copy the source file to a new destination
try:
    shutil.copy(source_file, destination_file)
except Exception as e:
    print(f'Error copying file: {e}')

# Create a new directory
try:
    os.makedirs(directory_path, exist_ok=True)
except Exception as e:
    print(f'Error creating directory: {e}')

# List files in the C:\\temp directory
try:
    print('Files in C:\\temp directory:')
    print(os.listdir('C:\\temp'))
except Exception as e:
    print(f'Error listing directory: {e}')