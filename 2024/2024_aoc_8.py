from collections import defaultdict
# %%


def print_map(map):
    for line in map:
        print(line)
        print("\n")

# %%

def add_antinodes_on_map(map, antinodes):
    new_map = []
    leni = len(map)
    for idi, line in enumerate(map):
        for idj, _ in enumerate(map[idi]):
            lenj = len(map[idi])
            if (idi, idj) in antinodes:
                line = line[:idj] + "#" + (line[idj + 1 : lenj] if idj < lenj else "")
        new_map.append(line)
    return new_map

map = add_antinodes_on_map(
    ["......", "......","......","......","......","......"],
    [(5,5), (1,1)]
)
print(map)

# %%

def aoc_1():
    with open("inputs/2024_input_aoc_8.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()
        map = [line.strip("\n") for line in lines]

        leni = len(lines)
        for idi, _ in enumerate(lines):
            for idj, current in enumerate(lines[idi]):
                lenj = len(lines[idi])
                if current != ".":
                    anti_nodes = []
                    
                    anti_nodes_1 = [
                        ((idi - abs(idi - i), idj - abs(idj - j)), (i + abs(idi - i), j + abs(idj - j)))
                        for i, j in zip(range(idi + 1, leni), range(idj + 1, lenj))
                        if lines[i][j] == current
                    ]
                    
                    anti_nodes_2 = [
                        ((idi + abs(idi - i), idj + abs(idj - j)), (i - abs(idi - i), j - abs(idj - j)))
                        for i, j in zip(range(idi - 1, 0), range(idj - 1, 0))
                        if lines[i][j] == current
                    ]
                    
                    anti_nodes_3 = [
                        ((idi - abs(idi - i), idj - abs(idj - j)), (i + abs(idi - i), j + abs(idj - j)))
                        for i, j in zip(range(idi + 1, leni), range(idj - 1, 0))
                        if lines[i][j] == current
                    ]
                    
                    anti_nodes_4 = [
                        ((idi + abs(idi - i), idj + abs(idj - j)), (i - abs(idi - i), j - abs(idj - j)))
                        for i, j in zip(range(idi - 1, 0), range(idj + 1, lenj))
                        if lines[i][j] == current
                    ]

                    anti_nodes = set(anti_nodes_1 + anti_nodes_2 + anti_nodes_3 + anti_nodes_4)
                    
                    print(anti_nodes)
                    # anti_nodes = set(node for node in anti_nodes if node[0] < leni and node[1] < lenj and node[0] >= 0 and node[1] >= 0)
                            
                            
                            
        print(anti_nodes)
                    


aoc_1()


# %%
def aoc_2():
    with open("inputs/2024_input_aoc_1.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()


aoc_2()
