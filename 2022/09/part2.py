from part1 import read_motions, touching


def make_moves(
    motion: str,
    visits: set[tuple[int, int]],
    knots: list,
):
    direction, distance = motion.split(" ")
    for _ in range(int(distance)):

        if direction == "L":
            knots[0][0] -= 1
        elif direction == "R":
            knots[0][0] += 1
        elif direction == "D":
            knots[0][1] -= 1
        elif direction == "U":
            knots[0][1] += 1

        for i in range(1, len(knots)):
            if not touching(knots[i - 1], knots[i]):
                knots = move(knots, i)

        visits.add(tuple(knots[-1]))

    return visits, knots


def move(knots: list, i: int) -> list:
    x = knots[i - 1][0] - knots[i][0]
    y = knots[i - 1][1] - knots[i][1]

    if x != 0:
        knots[i][0] += int(x / abs(x))

    if y != 0:
        knots[i][1] += int(y / abs(y))

    return knots


if __name__ == "__main__":
    knots = [[5, 5] for _ in range(10)]
    visits = {(5, 5)}

    motions = read_motions("motions.txt")
    for motion in motions:
        visits, knots = make_moves(motion, visits, knots)
    print(len(visits), "distinct tail positions")
