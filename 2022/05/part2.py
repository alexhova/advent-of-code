from part1 import read_crates, dictify, top_crates


def make_move(stacks: dict[str : list[str]], move: str):
    m = move.split(" ")
    move_count, move_from, move_to = int(m[1]), m[3], m[5]
    moved = stacks[move_from][-move_count:]
    stacks[move_to] += moved
    del stacks[move_from][-move_count:]


if __name__ == "__main__":
    rows, moves = read_crates()
    stacks = dictify(rows)
    for move in moves.splitlines():
        make_move(stacks, move)

    print(f"the top crates of each stack are {top_crates(stacks)}")
