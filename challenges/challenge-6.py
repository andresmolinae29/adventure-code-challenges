def read_file(file_route: str) -> list:

    with open(file_route, 'r') as file:

        lines = file.readlines()[0]

        return lines


def find_distinct(string: str, number_of_characters: int) -> str:

    init = 0
    final = number_of_characters
    
    for i in range(len(string)):

        if len(set(string[init:final])) == number_of_characters \
            and len(string[init:final]) == number_of_characters:

            return string[init:final]
            break

        else:

            init +=1
            final +=1


def find_index(string: str, pattern: str, number_of_characters: int) -> None:

    print(string.find(pattern) + number_of_characters)
    

def run():
    
    letters = read_file('../data/input-challenge-6.txt')

    distinct_value_four = find_distinct(letters, 4)
    distinct_value_fourteen = find_distinct(letters, 14)

    find_index(letters, distinct_value_four, 4)
    find_index(letters, distinct_value_fourteen, 14)
    

if __name__ == '__main__':
    run()