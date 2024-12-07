# %%
import re

WORD = "XMAS"


def find_xmas(line):
    if len(line) < len(WORD):
        return 0
    if re.match(WORD, line):
        return 1
    return 0


def aoc_1():
    fd = open("inputs/2024_input_aoc_4.txt")
    lines = fd.readlines()
    fd.close()

    result = 0
    leni = len(lines)
    for idi in range(0, leni):
        lenj = len(lines[idi])
        for idj in range(0, lenj):
            current = lines[idi][idj]
            if current != "X":
                continue

            checks = [
                # Check right
                find_xmas("".join(lines[idi][idj:])),
                # Check left
                find_xmas("".join(lines[idi][:idj + 1][::-1])),
                # Check up
                find_xmas("".join([lines[w][idj] for w in range(idi, -1, -1)])),
                # Check down
                find_xmas("".join([lines[w][idj] for w in range(idi, leni)])),
                # Check right down diagonal - both i j are incresing
                find_xmas("".join([lines[w][z] for w, z in zip(range(idi, leni), range(idj, lenj))])),
                # Check left up diagonal - both i j are decreasing
                find_xmas("".join([lines[w][z] for w, z in zip(range(idi, -1, -1), range(idj, -1, -1))])),
                # Check right up diagonal - i descreasing j incresing
                find_xmas("".join([lines[w][z] for w, z in zip(range(idi, -1, -1), range(idj, lenj))])),
                # Check left down diagonal - i incresing j descreasing
                find_xmas("".join([lines[w][z] for w, z in zip(range(idi, leni), range(idj, -1, -1))])),
            ]
            result += sum(checks)

    print(result)


aoc_1()


# %%
def aoc_2():
    fd = open("inputs/2024_input_aoc_4.txt")
    lines = fd.readlines()
    fd.close()

    result = 0
    leni = len(lines)
    for idi in range(0, leni):
        lenj = len(lines[idi])
        for idj in range(0, lenj):
            current = lines[idi][idj]
            if current != "A" or idi == 0 or idj == 0 or idi == leni - 1 or idj == lenj - 1:
                continue
            checks = 0
            if lines[idi - 1][idj - 1] == "M" and lines[idi + 1][idj + 1] == "S":
                checks += 1
            if lines[idi - 1][idj - 1] == "S" and lines[idi + 1][idj + 1] == "M":
                checks += 1
            if lines[idi - 1][idj + 1] == "M" and lines[idi + 1][idj - 1] == "S":
                checks +=1
            if lines[idi - 1][idj + 1] == "S" and lines[idi + 1][idj - 1] == "M":
                checks +=1
            print("\n")
            if checks == 2:
                result += 1

    print(result)


aoc_2()
