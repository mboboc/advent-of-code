
# %%
import sys, os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils import print_grid


def check_sides(grid, i, j):
    isize = len(grid)
    jsize = len(grid[0])
    neighbours = [
        (i - 1, j), # up
        (i + 1, j), # down
        (i, j - 1), # left
        (i, j + 1), # right
        (i - 1, j - 1), # corner_up_left
        (i + 1, j - 1), # corner_down_left
        (i - 1, j + 1), # corner_up_right
        (i + 1, j + 1), # corner_down_right
    ]

    count = 0
    for neighbour in neighbours:
        fst, scd = neighbour
        # print(fst, scd)
        if fst >= 0 and scd >= 0 and fst < isize and scd < jsize and grid[fst][scd] == "@":
            count += 1

    return count

def remove_paper(grid):
    new_grid = []
    accesible = 0
    for i, lst in enumerate(grid):
        new_lst = []
        for j, elem in enumerate(lst):
            if elem != "@":
                new_lst.append(elem)
                continue

            count = check_sides(grid, i, j)

            if count < 4:
                new_lst.append("x")
                accesible += 1
            else:
                new_lst.append(elem)

        new_grid.append(new_lst)

    return accesible, new_grid


def aoc_1():
    with open("inputs/2025_input_aoc_4.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()
        grid = [line.strip("\n") for line in lines]

        accesible, new_grid = remove_paper(grid)

        print_grid(new_grid)
        print(accesible)


aoc_1()

#%%
def aoc_2():
    with open("inputs/2025_input_aoc_4.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()
        grid = [line.strip("\n") for line in lines]

        accesible = -1
        result = 0
        new_grid = grid
        failsafe = 100
        while (accesible != 0):
            if failsafe < 1:
                print("Failsafe activated.")
                break
            print(accesible)
            accesible, new_grid = remove_paper(new_grid)
            result += accesible
            failsafe -= 1

        print(result)


aoc_2()
