from part1 import read_depths, count_increases


def make_clumps(depths):
    clumps = []
    for i in range(len(depths)):
        clumps.append(sum(depths[i:i + 3]))
    return clumps


if __name__ == "__main__":
    depths = read_depths()
    clumps = make_clumps(depths)
    increases = count_increases(clumps)

    print(f"{increases} increases counted")
