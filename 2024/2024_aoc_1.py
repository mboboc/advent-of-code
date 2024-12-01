from collections import defaultdict
# %%

def aoc_1():
    with open("inputs/2024_input_aoc_1.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        first_list = []
        second_list = []
        for line in lines:
            first, second = filter(None, line.split(" "))

            try:
                first_list.append(int(first))
                second_list.append(int(second))
            except ValueError:
                print("Input has mistakes.")

        first_list.sort()
        second_list.sort()

        result = 0
        for first, second in zip(first_list, second_list):
            diff = abs(first - second)
            result += diff

        print(result)


def aoc_2():
    with open("inputs/2024_input_aoc_1.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        first_list = []
        second_list = defaultdict(int)
        for line in lines:
            first, second = filter(None, line.split(" "))

            try:
                first_list.append(int(first))
                second_list[int(second)] = second_list[int(second)] + 1
            except ValueError:
                print("Input has mistakes.")

        result = 0
        for elem in first_list:
            result += elem * second_list[elem]

        print(result)

aoc_2()
