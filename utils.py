import os


def is_empty_file(filename):
    if os.path.getsize(filename):
        print("WARNING: File is empty!")

def print_grid(grid):
    for line in grid:
        print(line)

    print("\n\n\n")