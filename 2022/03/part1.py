import string

priorities = dict(zip(list(string.ascii_letters), range(1, 53)))


def read_rucksacks() -> list[str]:
    with open("rucksacks.txt") as f:
        return f.read().splitlines()


def common_item(rucksack: str) -> str:
    pocket_size = int(len(rucksack) / 2)
    pocket1, pocket2 = distinct(rucksack[:pocket_size]), distinct(rucksack[pocket_size:])
    for item in pocket1:
        if item in pocket2:
            return item


def distinct(items: str) -> str:
    return "".join(set(items))


if __name__ == "__main__":
    rucksacks = read_rucksacks()
    total_priority = 0
    for rucksack in rucksacks:
        item = common_item(rucksack)
        total_priority += priorities[item]

    print(f"total priority is {total_priority}")
