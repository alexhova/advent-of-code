def read_assignments() -> list[str]:
    with open("assignments.txt") as f:
        return f.read().splitlines()


def is_duplicated(pair: str) -> bool:
    ass1, ass2 = (stringify(i) for i in pair.split(","))
    if (ass1 in ass2) or (ass2 in ass1):
        return True
    return False


def stringify(assignment: str) -> str:
    first, last = assignment.split("-")
    return "".join(f" {str(i)} " for i in range(int(first), int(last) + 1))


if __name__ == "__main__":
    assignments = read_assignments()
    duplicate_count = 0
    for a in assignments:
        duplicate_count += is_duplicated(a)

    print(f"assignment pairs with duplicates: {duplicate_count}")
