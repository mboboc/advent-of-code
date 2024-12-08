# %%
from collections import defaultdict


def parse_input(lines):
    constrains = []
    updates = []
    is_update = False
    for line in lines:
        if line == "\n":
            is_update = True
            continue

        if is_update:
            updates.append(line.strip("\n").split(","))
        else:
            first, second = line.strip("\n").split("|")
            constrains.append((first, second))

    return constrains, updates


def print_dict(some_dict):
    for key, val in some_dict.items():
        print(key, val)


def get_contrains_mapping(constrains, update):
    # dict of {update: [list of after values]}
    update_to_after_map = defaultdict(list)
    for value in update:
        after_list = map(
            lambda item: item[1],
            filter(lambda item: item[0] == value and item[1] in update, constrains),
        )

        update_to_after_map[value] = list(after_list)

    return update_to_after_map


def swap(lst, idi, idj):
    if idi == idj:
        return lst

    new_list = []
    for idx, item in enumerate(lst):
        if idx == idi:
            new_list.append(lst[idj])
            continue
        if idx == idj:
            new_list.append(lst[idi])
            continue
        new_list.append(item)

    return new_list


def aoc_12():
    with open("inputs/2024_input_aoc_5.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()
        constrains, updates = parse_input(lines)

        results_aoc1 = []
        results_aoc2 = []
        for update in updates:
            initial_update = update.copy()
            constrains_mapping = get_contrains_mapping(constrains, update)

            idi = 0
            while idi < len(update):
                current = update[idi]
                idj = 0
                while idj < len(update):
                    comparing_with = update[idj]
                    if idj < idi and comparing_with in constrains_mapping[current]:
                        update = swap(update, idi, idj)
                        idi = 0
                        break
                    if idj > idi and comparing_with not in constrains_mapping[current]:
                        update = swap(update, idi, idj)
                        idi = 0
                        break
                    idj += 1
                idi += 1

            if update == initial_update:
                results_aoc1.append(update)

            if update != initial_update:
                results_aoc2.append(update)

        print(
            "Results 1:",
            sum([int(result[len(result) // 2]) for result in results_aoc1]),
        )
        print(
            "Results 2:",
            sum([int(result[len(result) // 2]) for result in results_aoc2]),
        )


aoc_12()
# %%
