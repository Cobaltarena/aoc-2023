import sys
from functools import reduce


def is_digit(char):
    return char >= "0" and char <= "9"


def get_number(line, starting_index, incrementation, limit, both_sides):
    ending_index = starting_index
    while ending_index != limit and is_digit(line[ending_index]):
        ending_index += incrementation
    if not is_digit(line[ending_index]):
        ending_index -= incrementation
    if both_sides:
        while starting_index != 0 and is_digit(line[starting_index]):
            starting_index -= incrementation
        if not is_digit(line[starting_index]):
            starting_index += incrementation
    if ending_index < starting_index:
        return int(line[ending_index : starting_index + 1])
    return int(line[starting_index : ending_index + 1])


def process_line(line, symbol_index, is_middle):
    if is_digit(line[symbol_index]):
        return [get_number(line, symbol_index, 1, len(line) - 1, True)]

    numbers = []

    if symbol_index >= 0 and is_digit(line[symbol_index - 1]):
        numbers.append(get_number(line, symbol_index - 1, -1, 0, False))

    if symbol_index < len(line) and is_digit(line[symbol_index + 1]):
        numbers.append(get_number(line, symbol_index + 1, 1, len(line) - 1, False))
    return numbers


def get_all_numbers_around_symbol(symbol_index, full_input, line_length, input_length):
    numbers = []

    if symbol_index > line_length:
        previous_line = full_input[
            (symbol_index - symbol_index % line_length)
            - line_length : (symbol_index + line_length - symbol_index % line_length)
            - line_length
        ]
        numbers += process_line(previous_line, symbol_index % line_length, False)

    current_line = full_input[
        (symbol_index - symbol_index % line_length) : (
            symbol_index + line_length - symbol_index % line_length
        )
    ]
    numbers += process_line(current_line, symbol_index % line_length, True)

    if symbol_index < input_length - line_length:
        next_line = full_input[
            (symbol_index - symbol_index % line_length)
            + line_length : (symbol_index + line_length - symbol_index % line_length)
            + line_length
        ]
        numbers += process_line(next_line, symbol_index % line_length, False)
    return numbers


def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    line_length = len(lines[0]) - 1
    full_input = "".join(lines).replace("\n", "")
    input_length = len(full_input)

    res_part_1 = 0
    numbers_found = []
    res_part_2 = 0

    for i in range(0, input_length):
        if full_input[i] != "." and not is_digit(full_input[i]):
            numbers = get_all_numbers_around_symbol(
                i, full_input, line_length, input_length
            )
            numbers_found += numbers
            res_part_1 += reduce((lambda x, y: x + y), numbers)
            if full_input[i] == "*" and len(numbers) == 2:
                res_part_2 += reduce((lambda x, y: x * y), numbers)

    print(f"part_1: {res_part_1}")
    print(f"part_2: {res_part_2}")


if __name__ == "__main__":
    main()
