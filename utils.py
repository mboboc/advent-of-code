import os


def is_empty_file(filename):
    if os.path.getsize(filename):
        print("WARNING: File is empty!")