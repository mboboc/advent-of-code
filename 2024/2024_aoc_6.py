# %%
def rotate90(cursor):
    if cursor == "^":
        return ">"
    if cursor == ">":
        return "v"
    if cursor == "v":
        return "<"
    if cursor == "<":
        return "^"


def find_start_cursor(puzzle_map: list[str]):
    for idi, line in enumerate(puzzle_map):
        for cursor in "^>v<":
            if (idj := line.find(cursor)) >= 0:
                return idi, idj, cursor


def is_obstacle_ahead(puzzle_map, idi, idj, cursor):
    if (
        idi + 1 < len(puzzle_map)
        and idi - 1 > -1
        and idj + 1 < len(puzzle_map[idi])
        and idj - 1 > -1
    ):
        if cursor == "^" and puzzle_map[idi - 1][idj] in ["#", "O"]:
            return True
        if cursor == ">" and puzzle_map[idi][idj + 1] in ["#", "O"]:
            return True
        if cursor == "v" and puzzle_map[idi + 1][idj] in ["#", "O"]:
            return True
        if cursor == "<" and puzzle_map[idi][idj - 1] in ["#", "O"]:
            return True

    return False


def get_path(puzzle_map):
    leni = len(puzzle_map)
    result = set()
    idi, idj, cursor = find_start_cursor(puzzle_map)

    while idi < leni and idj < len(puzzle_map[idi]) and idi >= 0 and idj >= 0:
        if is_obstacle_ahead(puzzle_map, idi, idj, cursor):
            cursor = rotate90(cursor)
            continue
        if cursor == "^":
            idi -= 1
        if cursor == ">":
            idj += 1
        if cursor == "v":
            idi += 1
        if cursor == "<":
            idj -= 1

        result.add((idi, idj))

    return result


def is_loop(puzzle_map, idi, idj, cursor):
    leni = len(puzzle_map)

    loop_counter = []
    while idi < leni and idj < len(puzzle_map[idi]) and idi >= 0 and idj >= 0:
        item = (idi, idj, cursor)
        if item in loop_counter:
            return 1
        else:
            loop_counter.append(item)
        if is_obstacle_ahead(puzzle_map, idi, idj, cursor):
            cursor = rotate90(cursor)
            continue
        if cursor == "^":
            idi -= 1
        if cursor == ">":
            idj += 1
        if cursor == "v":
            idi += 1
        if cursor == "<":
            idj -= 1

    return 0


def build_new_map(lines, idi, idj):
    new_map = []
    for idx, line in enumerate(lines):
        if idx == idi:
            line_list = list(line)
            line_list[idj] = "O"
            new_map.append("".join(line_list))
        else:
            new_map.append(line)

    return new_map


def print_map(puzzle_map):
    for line in puzzle_map:
        print(line)

    print("\n\n\n")


# %%
def aoc_1():
    with open("inputs/2024_input_aoc_6.txt") as fd:
        puzzle_map = fd.readlines()
        result = get_path(puzzle_map)
        print(len(result) - 1)


aoc_1()


# %%
def aoc_2():
    with open("inputs/2024_input_aoc_6.txt") as fd:
        puzzle_map = fd.readlines()

        path = get_path(puzzle_map)
        starti, startj, cursor = find_start_cursor(puzzle_map)
        result = 0

        for idx, (idi, idj) in enumerate(path):
            print(f"Count: {idx}")
            if idi == starti and idj == startj:
                continue

            new_map = build_new_map(puzzle_map, idi, idj)
            result += is_loop(new_map, starti, startj, cursor)

        print(result)


aoc_2()
