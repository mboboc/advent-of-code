# %%

def aoc_1():
    with open("inputs/2025_input_aoc_1.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        result = 0
        idx = 50
        strlen = 100
        for line in lines:
            rotation = line.strip("\n")
            letter = rotation[0]
            number = int(rotation[1:])

            if letter == "R":
                idx = (idx + number) % strlen
            elif letter == "L":
                idx = (idx - number) % strlen
            else:
                raise ValueError("Something is wrong.")

            if idx == 0:
                result += 1

        print(result)
aoc_1()

# %%

def aoc_2():
    with open("inputs/2025_input_aoc_1.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        result = 0
        idx = 50
        strlen = 100
        for line in lines:
            rotation = line.strip("\n")

            letter = rotation[0]
            number = int(rotation[1:])

            while (number > 0):
                if letter == "R":
                    idx += 1
                elif letter == "L":
                    idx -= 1
                else:
                    raise ValueError("Something is wrong.")

                if idx == strlen:
                    idx = 0
                if idx < 0:
                    idx = strlen - 1

                number -= 1
                if idx == 0:
                    result += 1

        print(result)
aoc_2()

