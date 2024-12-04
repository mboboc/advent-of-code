# %%
def is_level_safe(lvl_list, sign):
    for idx in range(1, len(lvl_list)):
        diff = lvl_list[idx] - lvl_list[idx - 1]

        if sign > 0 and diff not in [1, 2, 3]:
            return False

        if sign < 0 and diff not in [-1, -2, -3]:
            return False

    return True


def aoc_1():
    with open("inputs/2024_input_aoc_2.txt") as fd:
        lines = fd.readlines()

        safe = 0
        for line in lines:
            try:
                lvl_list = list(map(int, line.split(" ")))
            except ValueError:
                print("Input has mistakes.")

            sign = lvl_list[1] - lvl_list[0]
            if sign == 0:
                continue
            else:
                sign = sign / abs(sign)

            if is_level_safe(lvl_list, sign):
                safe += 1

        print(safe)


aoc_1()

# %%
import math


def is_lvl_safe(lvl_list: list[int]) -> bool:
    diff_sum = 0

    for idx in range(1, len(lvl_list)):
        diff = lvl_list[idx] - lvl_list[idx - 1]

        if (
            abs(diff) not in [1, 2, 3]
            or diff_sum
            and math.copysign(1, diff_sum) != math.copysign(1, diff)
        ):
            return False

        diff_sum += diff
    else:
        return True


def aoc_2():
    with open("inputs/2024_input_aoc_2.txt") as fd:
        lines = fd.readlines()

        safe = 0
        for line in lines:
            try:
                lvl_list = list(map(int, line.split(" ")))
            except ValueError:
                print("Input has mistakes.")

            ret = is_lvl_safe(lvl_list)
            if ret is True:
                safe += 1
            else:
                for idx in range(0, len(lvl_list)):
                    new_list = [lvl_list[i] for i in range(len(lvl_list)) if i != idx]
                    ret = is_lvl_safe(new_list)
                    if ret is True:
                        safe += 1
                        break

        print(safe)


aoc_2()
