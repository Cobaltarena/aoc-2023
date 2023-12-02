import sys
from functools import reduce


COLOR_TO_HALF_COLOR = {
    "red": "red",
    "blue": "lue",
    "green": "een"
}

GAMES = {}


def init_game():
    return {
        "red": 0,
        "lue": 0,
        "een": 0
    }.copy()


def process_game(game_id: int, sets: str):
    GAMES[game_id] = init_game()
    for set in sets:
        for current_step in set.split(','):
            new = int(current_step.split(' ')[1])
            stored = GAMES[game_id][current_step[-3:]]
            GAMES[game_id][current_step[-3:]] = new if new > stored else stored


def is_possible_game(game):
    return (game[COLOR_TO_HALF_COLOR["red"]] <= 12) and \
        (game[COLOR_TO_HALF_COLOR["green"]] <= 13) and \
        (game[COLOR_TO_HALF_COLOR["blue"]] <= 14)


def main():
    with open(sys.argv[1]) as f:
        lines = f.readlines()
    for line in lines:
        line = line[len("Game "):]
        [game_id, sets] = line[:-1].split(":", 2)
        process_game(int(game_id), sets.split(";"))
    res_part_1 = 0
    res_part_2 = 0

    for game_id, game in GAMES.items():
        if is_possible_game(game):
            res_part_1 += game_id
        res_part_2 += reduce((lambda x, y: x * y), game.values())

    print(f"part_1: {res_part_1}")
    print(f"part_2: {res_part_2}")


if __name__ == "__main__":
    main()
