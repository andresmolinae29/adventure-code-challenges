"""
--- Day 3: Rucksack Reorganization ---
One Elf has the important job of loading all of the rucksacks with supplies for the jungle journey. Unfortunately, that Elf didn't quite follow the packing instructions, and so a few items now need to be rearranged.

Each rucksack has two large compartments. All items of a given type are meant to go into exactly one of the two compartments. The Elf that did the packing failed to follow this rule for exactly one item type per rucksack.

The Elves have made a list of all of the items currently in each rucksack (your puzzle input), but they need your help finding the errors. Every item type is identified by a single lowercase or uppercase letter (that is, a and A refer to different types of items).

The list of items for each rucksack is given as characters all on a single line. A given rucksack always has the same number of items in each of its two compartments, so the first half of the characters represent items in the first compartment, while the second half of the characters represent items in the second compartment.

For example, suppose you have the following list of contents from six rucksacks:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
The first rucksack contains the items vJrwpWtwJgWrhcsFMMfFFhFp, which means its first compartment contains the items vJrwpWtwJgWr, while the second compartment contains the items hcsFMMfFFhFp. The only item type that appears in both compartments is lowercase p.
The second rucksack's compartments contain jqHRNqRjqzjGDLGL and rsFMfFZSrLrFZsSL. The only item type that appears in both compartments is uppercase L.
The third rucksack's compartments contain PmmdzqPrV and vPwwTWBwg; the only common item type is uppercase P.
The fourth rucksack's compartments only share item type v.
The fifth rucksack's compartments only share item type t.
The sixth rucksack's compartments only share item type s.
To help prioritize item rearrangement, every item type can be converted to a priority:

Lowercase item types a through z have priorities 1 through 26.
Uppercase item types A through Z have priorities 27 through 52.
In the above example, the priority of the item type that appears in both compartments of each rucksack is 16 (p), 38 (L), 42 (P), 22 (v), 20 (t), and 19 (s); the sum of these is 157.

Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?

Your puzzle answer was 8153.

The first half of this puzzle is complete! It provides one gold star: *

--- Part Two ---
As you finish identifying the misplaced items, the Elves come to you with another issue.

For safety, the Elves are divided into groups of three. Every Elf carries a badge that identifies their group. For efficiency, within each group of three Elves, the badge is the only item type carried by all three Elves. That is, if a group's badge is item type B, then all three Elves will have item type B somewhere in their rucksack, and at most two of the Elves will be carrying any other item type.

The problem is that someone forgot to put this year's updated authenticity sticker on the badges. All of the badges need to be pulled out of the rucksacks so the new authenticity stickers can be attached.

Additionally, nobody wrote down which item type corresponds to each group's badges. The only way to tell which item type is the right one is by finding the one item type that is common between all three Elves in each group.

Every set of three lines in your list corresponds to a single group, but each group can have a different badge item type. So, in the above example, the first group's rucksacks are the first three lines:

vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
And the second group's rucksacks are the next three lines:

wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
In the first group, the only item type that appears in all three rucksacks is lowercase r; this must be their badges. In the second group, their badge item type must be Z.

Priorities for these items must still be found to organize the sticker attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for the second group. The sum of these is 70.

Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types? """

import string
from functools import reduce

def read_file(file_route: str) -> dict:

    with open(file_route, 'r') as file:
        compartments: list = []

        lines = file.readlines()

        for line in lines:
            line_strip = line.strip()

            line_len = int(len(line_strip)/2)

            compartments.append([line_strip[:line_len], line_strip[line_len:]])

    return compartments


def letters_dict():

    start_count = 1
    dict_letters = {}

    for letter in string.ascii_letters:
        dict_letters[letter] = start_count

        start_count += 1

    return dict_letters


def prioritation(compartments: list) -> dict:

    letters_value = letters_dict()

    rucksack_priority = {}

    for compartment in compartments:

        words_in_commun = set([word for word in compartment[0] if word in compartment[1]])

        for word in words_in_commun:

            if word not in rucksack_priority:
                rucksack_priority[word] = [letters_value[word]]

            else:
                rucksack_priority.get(word).append(letters_value[word])

    return rucksack_priority


def total_prioritation_by_word(rucksack_priority: dict) -> dict:

    rucksack_prioritation_summarize = {key: sum(values) for key, values in rucksack_priority.items()}

    return rucksack_prioritation_summarize


def total_prioritation(rucksack_prioritation_summarize: dict):

    total = sum(rucksack_prioritation_summarize.values())

    print(f"The total value to prioritize is: {total}")


def read_file_part_two(file_route: str) -> dict:

    with open(file_route, 'r') as file:
        compartments: list = []

        lines = file.readlines()

        for line in lines:
            line_strip = line.strip()

            compartments.append(line_strip)

    return compartments


def group_elfs(compartments: list) -> dict:

    group_number = 0
    group_value = 0
    compartments_grouped = {}

    for compartment in compartments:

        if group_number not in compartments_grouped:
                compartments_grouped[group_number] = [set(compartment)]

        else:
            compartments_grouped.get(group_number).append(set(compartment))

        group_value += 1

        if group_value % 3 == 0:
            group_number += 1

    return compartments_grouped

def total(compartment_grouped: dict):

    sum = 0

    letter_value = letters_dict()

    for key, value in compartment_grouped.items():

        word = list(set.intersection(*value))[0]
        sum += letter_value.get(word)

    print(f"The total value per group is: {sum}")


def run():

    compartments = read_file("../data/input-challenge-3.txt")
    prioritation_dict = prioritation(compartments)
    total_prioritation_by_word_result = total_prioritation_by_word(prioritation_dict)
    total_prioritation(total_prioritation_by_word_result)

    compartments = read_file_part_two("../data/input-challenge-3.txt")
    grouped = group_elfs(compartments)
    total(grouped)


if __name__ == '__main__':
    run()
