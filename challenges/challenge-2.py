def read_file(file_route: str) -> dict:

    with open('../data/input-challenge-2.txt', 'r') as file:
        elf_dict = {}

        lines = file.readlines()

        for id, line in enumerate(lines):
            line_strip = line.strip()
            elf_dict[id] = line_strip.split(" ")

    return elf_dict


def strategy_guide() -> dict:

    strategy_dict = {
        "X": {"response": "A", "score": {
            "A": 3,
            "B": 0,
            "C": 6
        }},
        "Y": {"response": "B", "score": {
            "A": 6,
            "B": 3,
            "C": 0
        }},
        "Z": {"response": "C", "score": {
            "A": 0,
            "B": 6,
            "C": 3
        }},
    }

    strategy_dict_2 = {
        "X": {"score": 0, "response": {
            "A": "C",
            "B": "A",
            "C": "B"
        }},
        "Z": {"score": 6, "response": {
            "A": "B",
            "B": "C",
            "C": "A"
        }},
        "Y": {"score": 3, "response": {
            "A": "A",
            "B": "B",
            "C": "C"
        }}
        }

    scores = {
        "A": 1,
        "B": 2,
        "C": 3
    }

    return strategy_dict, strategy_dict_2, scores


def strategy_implementation(elf_dict: dict) -> int:

    strategy_dict, strategy_dict_2, scores = strategy_guide()

    score = 0
    score_2 = 0

    for key, value in elf_dict.items():

        stretegy_selection: dict = strategy_dict.get(value[1])
        response = stretegy_selection.get("response")
        score_round = scores.get(response) + stretegy_selection.get("score").get(value[0])

        score = score + score_round

    for key, value in elf_dict.items():

        stretegy_selection: dict = strategy_dict_2.get(value[1])
        response = stretegy_selection.get("response").get(value[0])
        score_round = scores.get(response) + stretegy_selection.get("score")

        score_2 = score_2 + score_round

    print(f"The total score according to the strategy is: {score}")
    print(f"The total score according to the strategy two is: {score_2}")


def run():

    elf_dict = read_file("../data/input-challenge-2.txt")
    strategy_implementation(elf_dict)


if __name__ == '__main__':
    run()
