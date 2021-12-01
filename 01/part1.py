def read_depths():
    depths = []
    with open("depths.txt") as f:
        for line in f:
            depths.append(int(line))
    return depths


def count_increases(depths):
    return sum([
        1 for i in range(len(depths)) if i != 0 and depths[i] > depths[i - 1]
    ])


if __name__ == "__main__":
    depths = read_depths()
    increases = count_increases(depths)

    print(f"{increases} increases counted")
