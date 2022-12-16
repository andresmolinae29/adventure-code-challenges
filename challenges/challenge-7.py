def read_file(file_route: str) -> list:

    with open(file_route, 'r') as file:

        lines = file.readlines()[0]

        return lines


def run():
    pass


if __name__ == '__main__':
    run()
    