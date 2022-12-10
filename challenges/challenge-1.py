def read_file(file_route: str) -> dict:

    with open(file_route, 'r') as file:
        elf_dict = {}
        elf_id = 1

        lines = file.readlines()

        for line in lines:

            line_strip = line.strip()

            if line_strip.isnumeric():

                if elf_id in elf_dict:
                    elf_dict[elf_id].append(int(line_strip))
                else:
                    elf_dict[elf_id] = [int(line_strip)]
            else:

                elf_id += 1

    elf_dict_summarize = {key: sum(values) for key, values in elf_dict.items()}

    return elf_dict_summarize


def get_top_values(elf_dict: dict, top_values: int) -> None:

    elf_dict_sorted = sorted(
        elf_dict.items(), key=lambda item: item[1], reverse=True
        )

    total_calories = 0

    for i in range(top_values):

        try:

            total_calories = total_calories + elf_dict_sorted[i][1]

            print(
                f"The elf {elf_dict_sorted[i][0]} top {i + 1} has {elf_dict_sorted[i][1]}")

        except:

            print("there is no value for this top")

    print(f"Total calories {total_calories}")


def run() -> None:

    elf_dict = read_file('../data/input-challenge-1.txt')
    get_top_values(elf_dict, 3)


if __name__ == '__main__':
    run()
