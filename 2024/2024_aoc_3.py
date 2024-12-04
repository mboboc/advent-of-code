# %%
import re


def aoc_1():
    with open("inputs/2024_input_aoc_3.txt") as fd:
        lines = fd.readlines()

        result = 0
        for line in lines:
            elems = re.findall(r"mul\((\d\d?\d?,\d\d?\d?)\)", line)
            for elem in elems:
                a, b = elem.split(",")
                result += int(a) * int(b)

        print(result)


aoc_1()


# %%
def aoc_2():
    with open("inputs/2024_input_aoc_3.txt") as fd:
        lines = fd.read()

        result = 0
        elems = re.findall(r"don't\(\)|do\(\)|mul\(\d\d?\d?,\d\d?\d?\)", lines)
        do = True
        for elem in elems:
            if elem == "do()":
                do = True
                continue

            if elem == "don't()":
                do = False
                continue

            if do:
                match = re.findall(r"mul\((\d\d?\d?,\d\d?\d?)\)", elem)
                if match:
                    a, b = match[0].split(",")
                    result += int(a) * int(b)

        print(result)


aoc_2()
