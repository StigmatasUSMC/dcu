#!/usr/bin/python3

import os
import shutil

from datetime import datetime

file_types = {
    'Documents': ['doc', 'xls', 'ppt', 'docx', 'xlsx', 'pptx', 'pdf', 'txt'],
    'Music': ['mp3', 'mp4', 'm4a', 'wav', 'flac'],
    'Pictures': ['jpg', 'jpeg', 'gif', 'png', 'bmp'],
    'Videos': ['m4v', 'avi', 'mkv'],
}

path = r'c:\Users\n_sha\Desktop'
destination = r'c:\Users\n_sha'

if not os.path.exists(destination):
    os.makedirs(destination)


# Sorting function
def filter_files1(file_list):
    # Sorted dictionary, contains an array of types,
    # each with a corresponding matching file list
    sorted_files = {}
    # Iterate over each key (type)
    for category in file_types:
        # Create type key before trying to populate it
        sorted_files[category] = []
        # Iterate over the extension list in each type
        for extension in file_types[category]:
            # Iterate over the file list (done for each 'type/extension' pair)
            for file in file_list:
                # Same filtering from before, done per file,
                # for every extension, for every type
                if file.endswith('.' + extension):
                    sorted_files[category].extend([file])
    return sorted_files


# Sorting function (ver 2)
def filter_files2(file_list):
    # Sorted dictionary, contains an array of types,
    # each with a corresponding matching file list
    sorted_files = {}
    # Iterate over each key (types) and each value (extension lists)
    for category, extensions in list(file_types.items()):
        # Create type key before trying to populate it
        sorted_files[category] = []
        # Iterate over the extension list in each type
        for extension in extensions:
            # Iterate over the file list (done for each 'type/extension' pair)
            for file in file_list:
                # Same filtering from before, done per file,
                # for every extension, for every type
                if file.endswith('.' + extension):
                    sorted_files[category].extend([file])
    return sorted_files


# Move function
def move_files1(file_list):
    # For each type category in the sorted dictionary
    for category in file_list:
        # Iterate over the files in the category
        for file in file_list[category]:
            # Move the file to the destination (based on category)
            # These should instead be using `os.path.join()`
            print('Moving FROM: ' + path + '\\' + file + '\n' +
                  'Moving TO: ' + destination + '\\' + category + '\\' + file)
            shutil.move(path + '\\' + file, destination + '\\' + category)


# Move function (improved)
def move_files2(file_list):
    # For each type category in the sorted dictionary
    for category in file_list:
        # Iterate over the files in the category
        for file in file_list[category]:
            # Move the file to the destination (based on category)
            # Using `os.path.join()` means no more '\' or '/' issues
            print('Moving From: ' + os.path.join(path, file) + '\n' +
                  'Moving To: ' + os.path.join(destination, category, file))
            try:
                shutil.move(os.path.join(path, file),
                            os.path.join(destination, category))
            except Exception as e:
                print(e)


if __name__=='__main__':
    # Chain them all together instead of using intermediates
    move_files2(filter_files1(os.listdir(path)))
