# %%
def get_signs(value, padding_size) -> str:
    is_zero = True if not value else False

    binary_string = ""
    while value > 0:
        quotient = value // 2
        reminder = value % 2
        binary_string = str("+" if not reminder else "*") + binary_string
        value = quotient

    if is_zero:
        binary_string = "+"

    while len(binary_string) < padding_size:
        binary_string = "+" + binary_string

    return binary_string


def get_sum_and_string_equation(values, signs):
    result = values[0]
    equation_str = str(result)
    for value, sign in zip(values[1:], signs):
        if sign == "+":
            result += value
        if sign == "*":
            result *= value

        equation_str += f" {sign} "
        equation_str += str(value)

    return result, equation_str


def aoc_1():
    with open("inputs/2024_input_aoc_7.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        result = 0
        for line in lines:
            total, string_values = line.strip("\n").split(":")
            total = int(total)
            test_values = list(
                map(lambda val: int(val), filter(None, string_values.split(" ")))
            )

            binary_value = pow(2, len(test_values) - 1)
            for idx in range(0, binary_value):
                signs = get_signs(idx, len(get_signs(binary_value - 1, 0)))
                test_sum, equation_str = get_sum_and_string_equation(test_values, signs)
                # print(test_sum, ":", equation_str)

                if test_sum == total:
                    result += total
                    break

        print(result)


aoc_1()


# %%
def get_signs(value, padding_size) -> str:
    is_zero = True if not value else False

    ternary_string = ""
    while value > 0:
        quotient = value // 3
        reminder = value % 3
        if reminder == 0:
            ternary_string = "+" + ternary_string
        if reminder == 1:
            ternary_string = "*" + ternary_string
        if reminder == 2:
            ternary_string = "|" + ternary_string

        value = quotient

    if is_zero:
        ternary_string = "+"

    while len(ternary_string) < padding_size:
        ternary_string = "+" + ternary_string

    return ternary_string


def get_sum_and_string_equation(values, signs):
    result = values[0]
    equation_str = str(result)
    for value, sign in zip(values[1:], signs):
        if sign == "+":
            result += value
        if sign == "*":
            result *= value
        if sign == "|":
            result = int(str(result) + str(value))
        equation_str += f" {sign} "
        equation_str += str(value)

    return result, equation_str


def aoc_2():
    with open("inputs/2024_input_aoc_7.txt", "r", encoding="utf-8") as fd:
        lines = fd.readlines()

        result = 0
        for idx, line in enumerate(lines):
            print(idx)
            total, string_values = line.strip("\n").split(":")
            total = int(total)
            test_values = list(
                map(lambda val: int(val), filter(None, string_values.split(" ")))
            )

            ternary_value = pow(3, len(test_values) - 1)
            for idx in range(0, ternary_value):
                signs = get_signs(idx, len(get_signs(ternary_value - 1, 0)))
                test_sum, equation_str = get_sum_and_string_equation(test_values, signs)
                # print(test_sum, ":", equation_str)

                if test_sum == total:
                    result += total
                    break

        print(result)


aoc_2()
