
import re

# %%
def aoc_1():
    with open("inputs/2025_input_aoc_3.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()
        result = 0
        for line in lines:
            max1 = 0
            max2 = 0

            line = line.strip("\n")
            for idx, char in enumerate(line):
                num = int(char)
                if num > max1 and idx != len(line) - 1:
                    max1 = num
                    max2 = 0
                elif num > max2:
                    max2 = num
            result += max1 * 10 + max2

        print(result)


aoc_1()

#%%
def list_to_num(lst):
    size = len(lst)

    num = 0
    unit = 1
    for idx in range(size - 1, -1, -1):
        num += lst[idx] * unit

        unit *= 10

    return num

#%%


def aoc_2():
    with open("inputs/2025_input_aoc_3.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        final = 0
        size = 12
        for line in lines:
            line = line.strip("\n")
            latest_digit_idx = None
            strlen = len(line)

            nums = [int(char) for char in line]

            result = []
            for idx in range(0, size):
                if latest_digit_idx is not None:
                    start = latest_digit_idx + 1
                else:
                    start = 0
                end = strlen - size + idx + 1
                # print(start, end)

                i, current_max = max(enumerate(nums[start:end]), key=lambda x: x[1])
                # print(f"Found ({start + i}) {current_max}")
                result.append(current_max)
                latest_digit_idx = start + i

            # print(line, list_to_num(result))
            final += list_to_num(result)
        print(final)

aoc_2()

# %%
