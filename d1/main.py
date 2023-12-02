import sys
import re

words_to_number = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def find_numbers_in_line(line: str):
    search = re.search("^.*?([0-9]).*?([0-9]{0,1})[^0-9]*$", line)
    if not search:
        return None
    [last_number, first_number] = [i for i in search.groups()[::-1]]
    if last_number == '':
        last_number = first_number
    return int(last_number) + int(first_number) * 10


def sanitize_line(line):
    sanitized_line = ""
    i = 0
    while i < len(line):
        prefix = list(filter(lambda prefix: line.startswith(prefix, i), words_to_number.keys()))
        if prefix:
            sanitized_line += str(words_to_number[prefix[0]])
        else:
            sanitized_line += line[i]
        i += 1
    return sanitized_line


def main():
    lines = []
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    res = 0

    for i in lines:
        sanitized_line = sanitize_line(i)
        res_for_line = find_numbers_in_line(sanitized_line)
        res += res_for_line

    print(f"part2: {res}")


if __name__ == "__main__":
    main()
