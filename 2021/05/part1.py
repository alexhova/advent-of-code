def points(line):
    x1, y1, x2, y2 = line.replace(" -> ", ",").strip().split(",")
    return (int(x1), int(y1)), (int(x2), int(y2))


def walk(start, end):
    if start[0] == end[0]:
        step = 1 if start[1] < end[1] else -1
        return [(start[0], y) for y in range(start[1], end[1] + step, step)]
    if start[1] == end[1]:
        step = 1 if start[0] < end[0] else -1
        return [(x, start[1]) for x in range(start[0], end[0] + step, step)]


def count(walked, counts):
    for point in walked:
        counts[str(point)] = counts.get(str(point), 0) + 1


def overlaps(counts):
    return sum([n >= 2 for n in counts.values()])


if __name__ == "__main__":
    counts = {}
    with open("vents.txt") as f:
        for line in f:
            start, end = points(line)
            walked = walk(start, end)
            if walked:
                count(walked, counts)
    print(f"number of overlapping vents is {overlaps(counts)}")
