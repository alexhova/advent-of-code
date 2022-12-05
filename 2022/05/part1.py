def read_crates() -> tuple[str, str]:
    with open("crates.txt") as f:
        return f.read().split("\n\n")


def dictify(rows: str) -> dict[str : list[str]]:
    rows = rows.split("\n")
    line_length = len(rows[0])
    stack_count = int(rows.pop().strip().split(" ")[-1])
    stacks = dict(
        zip((str(i + 1) for i in range(stack_count)), ([] for _ in range(stack_count)))
    )

    for row in reversed(rows):
        stack_number = 1
        for i in range(0, line_length - 2, 4):
            if row[i + 1] != " ":
                stacks[str(stack_number)].append(row[i + 1])
            stack_number += 1

    return stacks


def make_move(stacks: dict[str : list[str]], move: str):
    m = move.split(" ")
    move_count, move_from, move_to = int(m[1]), m[3], m[5]
    for _ in range(move_count):
        stacks[move_to].append(stacks[move_from].pop())


def top_crates(stacks: dict[str : list[str]]) -> str:
    return "".join(i[-1] for i in stacks.values())


if __name__ == "__main__":
    rows, moves = read_crates()
    stacks = dictify(rows)
    for move in moves.splitlines():
        make_move(stacks, move)

    print(f"the top crates of each stack are {top_crates(stacks)}")
