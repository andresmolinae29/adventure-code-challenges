from collections.abc import Callable

def read_file(file_route: str) -> list:

    with open(file_route, 'r') as file:

        lines = file.readlines()

        zones = []

        for line in lines:

            line_strip = line.strip()

            zones.append(line_strip)

        return zones


def split_info(zones_list: list) -> list:

    return [zone.split(',') for zone in zones_list]


def set_ranges(l: str) -> set:

    l = l.split("-")

    return set(range(int(l[0]), int(l[-1]) + 1))


def compare_subset(set1: set, set2: set) -> bool:

    return set1.issubset(set2) or set2.issubset(set1)


def compare_overlap(set1: set, set2: set) -> bool:

    return len(set1.intersection(set2)) > 0


def count_subsets(zone_list: list, overlaptype: Callable[[set, set], bool]) -> int:

    number_of_subsets = 0

    split_zones = split_info(zone_list)

    for zone in split_zones:

        zone_set_1, zone_set_2 = set_ranges(zone[0]), set_ranges(zone[1])

        is_subset = overlaptype(zone_set_1, zone_set_2)

        if is_subset:
            number_of_subsets += 1

    return number_of_subsets


def run():

    zone_list = read_file("../data/input-challenge-4.txt")
    number_of_subsets = count_subsets(zone_list, compare_subset)
    print(f"the number of repetead zones is: {number_of_subsets}")

    number_overlaps = count_subsets(zone_list, compare_overlap)
    print(f"the number of overlap zones is: {number_overlaps}")


if __name__ == '__main__':
    run()
