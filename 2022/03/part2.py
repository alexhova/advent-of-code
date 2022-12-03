from part1 import read_rucksacks, distinct, priorities


def common_item(group: list[str]) -> str:
    for item in distinct(group[0]):
        if item in group[1] and item in group[2]:
            return item


if __name__ == "__main__":
    rucksacks = read_rucksacks()
    total_priority = 0
    group_indexes = range(0, len(rucksacks) - 2, 3)
    for i in group_indexes:
        item = common_item(rucksacks[i : i + 3])
        total_priority += priorities[item]

    print(f"total priority is {total_priority}")
