import numpy as np
from collections.abc import Callable

def read_file(file_route: str) -> list:

    with open(file_route, 'r') as file:

        lines = file.readlines()

        result = []

        for line in lines:

            line_strip = line.strip()

            result.append(list(line_strip))

        return np.array(result)


def get_edges_count(tree_list: list) -> int:

   return len(tree_list) * 2 + ( len(tree_list) - 2 ) * 2 


def count_high_tree(col_list: list, row_list: list, top: int, under: int) -> int:

    if (all(col_list[:top])):
        return 1

    elif (all(col_list[top+1:])):
        return 1
    
    elif (all(row_list[:under])):
        return 1
    
    elif (all(row_list[under+1:])):
        return 1

    else:
        return 0


def get_tree_view(col_list: list, row_list: list, top: int, under: int) -> int:

    def inner_count(l: list) -> int:
        count = 0

        for i in l:
            if not i:
                count += 1
                break

            else:
                count += 1

        return count

    col_up = inner_count(col_list[:top][::-1])
    col_down = inner_count(col_list[top+1:])
    row_left = inner_count(row_list[:under][::-1])
    row_right = inner_count(row_list[under+1:])

    return col_up * col_down * row_left * row_right

def iter(tree_list: list, fn: Callable) -> int:

    totals: list = []

    x = 0
    y = 0

    max_len = len(tree_list) -1
    range_lines = range(len(tree_list))

    for _ in range_lines:

        y = 0

        for _ in range_lines:

            if x != 0 and y != 0 and x != max_len and y != max_len:

                cols = list(tree_list[:, y])
                rows = list(tree_list[x, :])
                value = tree_list[x, y]
                    
                result_col = list(map(lambda x: value > x, cols))
                result_row = list(map(lambda x: value > x, rows))

                totals.append(fn(result_col, result_row, x, y))

            y += 1

        x += 1

    return totals


def run():
    tree_list = read_file("../data/input-challenge-8.txt")
    edge_trees = get_edges_count(tree_list)
    total_trees = iter(tree_list, count_high_tree)

    total_view = iter(tree_list, get_tree_view)

    print(sum(total_trees) + edge_trees)
    print(max(total_view))


if __name__ == '__main__':
    run()