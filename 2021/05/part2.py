from part1 import points, walk, count, overlaps


def walk_diagonally(start, end):
    walked = walk(start, end)
    if walked:
        return walked
    if abs(start[0] - end[0]) == abs(start[1] - end[1]):
        x_step = 1 if start[0] < end[0] else -1
        y_step = 1 if start[1] < end[1] else -1
        xs = range(start[0], end[0] + x_step, x_step)
        ys = range(start[1], end[1] + y_step, y_step)
        return zip(xs, ys)


counts = {}
with open("vents.txt") as f:
    for line in f:
        start, end = points(line)
        walked = walk_diagonally(start, end)
        if walked:
            count(walked, counts)
print(f"number of overlapping vents is {overlaps(counts)}")
