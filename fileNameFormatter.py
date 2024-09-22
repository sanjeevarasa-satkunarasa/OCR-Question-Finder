import os

def replace_spaces_in_filenames(directory):
    for filename in os.listdir(directory):
        if ' ' in filename:
            new_filename = filename.replace(' ', '_')
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_filename))
            print(f'Renamed: {filename} -> {new_filename}')

# Replace 'your_directory_path' with the path to your directory
replace_spaces_in_filenames('1T Files')
