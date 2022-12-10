def read_motions(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


def move(
    motion: str,
    visits: set[tuple[int, int]],
    head: list[int, int],
    tail: list[int, int],
):
    direction, distance = motion.split(" ")
    for _ in range(int(distance)):
        if direction == "L":
            head[0] -= 1
            if not touching(head, tail):
                tail = [head[0] + 1, head[1]]
                visits.add(tuple(tail))
        elif direction == "R":
            head[0] += 1
            if not touching(head, tail):
                tail = [head[0] - 1, head[1]]
                visits.add(tuple(tail))
        elif direction == "D":
            head[1] -= 1
            if not touching(head, tail):
                tail = [head[0], head[1] + 1]
                visits.add(tuple(tail))
        elif direction == "U":
            head[1] += 1
            if not touching(head, tail):
                tail = [head[0], head[1] - 1]
                visits.add(tuple(tail))

    return visits, head, tail


def touching(head: list[int, int], tail: list[int, int]) -> bool:
    if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
        return True
    return False


if __name__ == "__main__":
    head = [0, 0]
    tail = [0, 0]
    visits = {(0, 0)}

    motions = read_motions("motions.txt")
    for motion in motions:
        visits, head, tail = move(motion, visits, head, tail)
    print(len(visits), "distinct tail positions")
