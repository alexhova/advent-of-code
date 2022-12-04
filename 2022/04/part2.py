from part1 import read_assignments


def is_overlapped(pair: str) -> bool:
    ass1, ass2 = (listify(i) for i in pair.split(","))
    if len(ass1 + ass2) > len(set(ass1 + ass2)):
        return True
    return False


def listify(assignment: str) -> list[int]:
    first, last = assignment.split("-")
    return list(range(int(first), int(last) + 1))


if __name__ == "__main__":
    assignments = read_assignments()
    overlap_count = 0
    for a in assignments:
        overlap_count += is_overlapped(a)

    print(f"overlapping assignment pairs: {overlap_count}")
