import argparse
from datetime import datetime
import os
import shutil
from pathlib import Path

template = """
import re

# %%
def aoc_1():
    with open("{}", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

aoc_1()

#%%
def aoc_2():
    with open("{}", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

aoc_2()
"""


def main():
    current_year = datetime.now().year

    parser = argparse.ArgumentParser(
        prog="start_day",
        description="Creates templates files for a day in Advent of Code."
    )
    parser.add_argument("-d", "--day", type=int, required=True)
    parser.add_argument("-y", "--year", type=int)

    args = parser.parse_args()

    if not args.year:
        print(f"Year was not provided... using current year {current_year}")
        args.year = current_year
    elif args.year > current_year or args.year < 2000:
        print("Invalid year.")

    if args.day < 0 or args.day > 31:
        print("Invalid day")

    directory = Path(f"{args.year}")
    os.makedirs(directory, exist_ok=True)

    input_directory = Path("inputs")
    os.makedirs(input_directory, exist_ok=True)
    input_filename = input_directory / f"{args.year}_input_aoc_{args.day}.txt"

    filepath = directory / f"{args.year}_aoc_{args.day}.py"
    with open(filepath, 'w', encoding="utf-8") as fd:
        fd.write(template.format(input_filename, input_filename))

    input_filename = directory / input_filename
    input_filename.touch(exist_ok=True)

    print(f"Successfully created {filepath}")


if __name__ == "__main__":
    main()
