import sys


def init_next_games(starting_index, times):
    for i in range(starting_index + 1, starting_index + 1 + times):
        if i not in GAMES:
            GAMES[i] = {"count": GAMES[starting_index]["count"], "res": 0}
        else:
            GAMES[i]["count"] += GAMES[starting_index]["count"]


def process_line(line, index):
    winning_numbers, actual_numbers = line.split("|", 1)
    winning_numbers = sorted(list(filter(None, winning_numbers.split(" "))))
    actual_numbers = sorted(list(filter(None, actual_numbers.split(" "))))
    numbers_found = list(filter((lambda x: x in winning_numbers), actual_numbers))
    res = pow(2, len(numbers_found) - 1)
    if index not in GAMES:
        GAMES[index] = {"count": 1, "res": res if res >= 1 else 0}
    else:
        GAMES[index]["res"] = res if res >= 1 else 0
        GAMES[index]["count"] += 1

    init_next_games(index, len(numbers_found))
    return res if res >= 1 else 0


def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    res_part_1 = 0
    res_part_2 = 0
    global MAX_GAMES
    global GAMES
    GAMES = {}
    MAX_GAMES = len(lines)
    for i in range(MAX_GAMES):
        process_line(lines[i][:-1], i + 1)  # 1-indexed

    res_part_1 = sum(val["res"] for val in GAMES.values())
    res_part_2 = sum(val["count"] for val in GAMES.values())

    print(f"part_1: {res_part_1}")
    print(f"part_1: {res_part_2}")


if __name__ == "__main__":
    main()
