def read_trees() -> list[str]:
    with open("trees.txt") as f:
        return f.read().splitlines()


def count_visible(trees: list[str]) -> int:
    row_count = len(trees)
    col_count = len(trees[0])
    visible_count = 0

    for i in range(row_count):
        for j in range(col_count):
            if i in [0, row_count - 1] or j in [0, col_count - 1]:
                visible_count += 1
                continue
            visible_count += visible(i, j, trees)

    return visible_count


def visible(row: int, col: int, trees: list[str]) -> bool:
    row_count = len(trees)
    col_count = len(trees[0])
    tree_height = int(trees[row][col])

    if (
        # up
        not bool(sum(True for i in range(row) if int(trees[i][col]) >= tree_height))
        # down
        or not bool(
            sum(
                True
                for i in range(row + 1, col_count)
                if int(trees[i][col]) >= tree_height
            )
        )
        # left
        or not bool(sum(True for i in range(col) if int(trees[row][i]) >= tree_height))
        # right
        or not bool(
            sum(
                True
                for i in range(col + 1, row_count)
                if int(trees[row][i]) >= tree_height
            )
        )
    ):
        return True

    return False


if __name__ == "__main__":
    trees = read_trees()
    visible_count = count_visible(trees)
    print(f"{visible_count} visible trees")
