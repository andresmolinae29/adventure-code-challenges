import re
from collections.abc import Callable


def read_file(file_route: str) -> list:

    with open(file_route, 'r') as file:

        lines = file.readlines()

        result = []

        for line in lines:

            line_strip = line.strip()

            result.append(line_strip)

        return result


def create_dict_input_1(l: list) -> dict[list]:

    cargo = {key: [] for key in range(1, 10)}

    for line in l[:-1]:

        list_line = re.findall('.{1,4}', line)

        for id, value in enumerate(list_line):

            value_strip = value.strip()

            if len(value_strip):
                cargo.get(id + 1).append(value_strip)

    {key: value.reverse() for key, value in cargo.items()}

    return cargo


def create_mov_list(l: list) -> list:

    movs = []

    for line in l:

        line_clean = re.split('\D+', line)[1:]
        movs.append(line_clean)

    return movs


def movs_logic(cargo_dict, moves_, from_, to_) -> None:

    for move in range(int(moves_)):

        remove_value = cargo_dict.get(int(from_)).pop()

        cargo_dict.get(int(to_)).append(remove_value)


def apply_movs(cargo_dict: dict, movs_list: list, movs_logic: Callable[[int, int, int], None]) -> dict:

    for move in movs_list:

        movs_logic(cargo_dict, *move)

    return cargo_dict


def movs_logic_2(cargo_dict, moves_, from_, to_) -> None:

    remove_slice: list = cargo_dict.get(int(from_))[-int(moves_):]

    # print("Piece remove", moves_, remove_slice)

    del cargo_dict.get(int(from_))[-int(moves_):]

    # print("Before insert" , cargo_dict[int(to_)])

    cargo_dict[int(to_)] = cargo_dict.get(int(to_)) + remove_slice

    # print("After insert", cargo_dict[int(to_)])


def print_result(dict_result: dict) -> None:

    result = []

    for key, value in dict_result.items():

        result.append(value[-1][1])

    print("".join(result))

def run():

    cargo_list = read_file("../data/challenge-5/input-1.txt")
    move_list = read_file("../data/challenge-5/input-2.txt")

    cargo_list_adjusted = create_dict_input_1(cargo_list)
    move_list_adjusted = create_mov_list(move_list)

    cargo_dict_after_movs = apply_movs(cargo_list_adjusted, move_list_adjusted, movs_logic)
    print_result(cargo_dict_after_movs)

    cargo_list_adjusted = create_dict_input_1(cargo_list)
    cargo_dict_after_movs = apply_movs(cargo_list_adjusted, move_list_adjusted, movs_logic_2)
    print_result(cargo_dict_after_movs)


if __name__ == '__main__':
    run()