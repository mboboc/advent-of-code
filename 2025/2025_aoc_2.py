
import re

# %%

def is_valid(num: int):
    num_str = str(num)
    n = len(num_str)

    if num < 11:
        return True

    if num in [11, 22, 33, 44, 55, 66, 77, 88, 99]:
        return False
    elif n == 2:
        return True

    if n % 2 == 1:
        return True

    idx = 0
    half = n // 2
    while (idx < half):
        if num_str[idx] != num_str[half + idx]:
            return True
        idx += 1

    return False

assert is_valid(11) is False
assert is_valid(1010) is False
assert is_valid(1188511885) is False
assert is_valid(222222) is False
assert is_valid(446446) is False
assert is_valid(38593859) is False
assert is_valid(12345643) is True
assert is_valid(1012) is True
assert is_valid(1188511880) is True

def aoc_1():
    with open("inputs/2025_input_aoc_2.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()
        intervals = lines[0].split(",")

        result = 0
        for interval in intervals:
            start, end = interval.split("-")
            count = int(start)
            while count <= int(end):
                if not is_valid(count):
                    result += count
                count += 1

        print(result)

aoc_1()


#%%


def is_invalid(num: int):
    string = str(num)
    strlen = len(string)

    if strlen == 1:
        return False

    if strlen == 2:
        return string[0] == string[1]

    for pattern_size in range(1, strlen):
        if strlen % pattern_size == 0:
            if string == string[:pattern_size] * (strlen // pattern_size):
                return True

    return False

assert is_invalid(565656) is True
assert is_invalid(1) is False
assert is_invalid(11) is True
assert is_invalid(111) is True
assert is_invalid(12) is False
assert is_invalid(0) is False
assert is_invalid(1212121212) is True
assert is_invalid(81438143) is True
assert is_invalid(101101) is True


def aoc_2():
    with open("inputs/2025_input_aoc_2.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()
        intervals = lines[0].split(",")


        result = 0
        for interval in intervals:
            start, end = interval.split("-")
            count = int(start)
            while count <= int(end):
                if is_invalid(count):
                    # print(count)
                    result += count
                count += 1
        print(result)



aoc_2()

# %%
