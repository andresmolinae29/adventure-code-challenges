def read_file(file_route: str) -> list:

    with open(file_route, 'r') as file:

        lines = file.readlines()

        result = []

        for line in lines:

            line_strip = line.strip()

            result.append(line_strip)

        return result


