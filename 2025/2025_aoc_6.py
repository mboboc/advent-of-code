
import re

# %%
from math import prod

def aoc_1():
    with open("inputs/2025_input_aoc_6.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        split_lines = []
        for line in lines[:-1]:
            split_lines.append(line.strip("\n").split())

        operands = list(zip(*split_lines))
        operators = lines[-1].strip("\n").split()

        result = 0
        for idx, op in enumerate(operators):
            nums = [int(i) for i in operands[idx]]

            if op == "+":
                result += sum(nums)
            elif op == "*":
                result += prod(nums)

        print(result)


aoc_1()

#%%
from itertools import zip_longest
from itertools import groupby


def aoc_2():
    with open("inputs/2025_input_aoc_6.txt", "r", encoding="utf-8") as fd:
        content = fd.readlines()
        operations = content[-1].split()
        lines = [line.strip("\n") for line in content[:-1]]
        operands = list(zip_longest(*lines, fillvalue=" "))
        nums = ["".join(op).strip() for op in operands]

        groups = [list(g) for k, g in groupby(nums, key=lambda x: x != "") if k]

        result = 0
        for idx, op in enumerate(operations):
            nums = [int(i) for i in groups[idx]]
            print(nums)

            if op == "+":
                result += sum(nums)
            elif op == "*":
                result += prod(nums)

        print(result)
aoc_2()

