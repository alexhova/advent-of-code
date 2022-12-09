from part1 import read_trees
from math import prod


def scenic_scores(trees: list[str]) -> list[int]:
    row_count = len(trees)
    col_count = len(trees[0])
    scores = []

    for i in range(row_count):
        for j in range(col_count):
            if i in [0, row_count - 1] or j in [0, col_count - 1]:
                continue
            scores.append(calc_score(i, j, trees))

    return scores


def calc_score(row: int, col: int, trees: list[str]) -> int:
    row_count = len(trees)
    col_count = len(trees[0])
    tree_height = int(trees[row][col])
    scores = [0] * 4

    # up
    for i in reversed(range(row)):
        scores[0] += 1
        if int(trees[i][col]) >= tree_height:
            break
    # down
    for i in range(row + 1, col_count):
        scores[1] += 1
        if int(trees[i][col]) >= tree_height:
            break
    # left
    for i in reversed(range(col)):
        scores[2] += 1
        if int(trees[row][i]) >= tree_height:
            break
    # right
    for i in range(col + 1, row_count):
        scores[3] += 1
        if int(trees[row][i]) >= tree_height:
            break

    return prod(scores)


if __name__ == "__main__":
    trees = read_trees()
    scores = scenic_scores(trees)
    print(f"maximum scenic score is {max(scores)}")
