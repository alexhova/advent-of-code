from part1 import read_depths, count_increases


def make_clumps(depths):
    clumps = []
    for i in range(len(depths)):
        clump = depths[i:i + 3]
        if len(clump) != 3:
            return clumps
        clumps.append(sum(clump))


if __name__ == "__main__":
    depths = read_depths()
    clumps = make_clumps(depths)
    increases = count_increases(clumps)

    print(f"{increases} increases counted")
