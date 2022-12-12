from part1 import read_signals


def draw(x, cycle):
    if cycle % 40 - 1 in [x - 1, x, x + 1]:
        return "#"
    return "."


if __name__ == "__main__":
    signals = read_signals("signals.txt")
    x = 1
    cycle = 0
    picture = ""

    for signal in signals:
        cycle += 1
        picture += draw(x, cycle)
        if signal.split(" ")[0] == "addx":
            cycle += 1
            picture += draw(x, cycle)
            x += int(signal.split(" ")[1])

    for i in range(0, 240, 40):
        print(picture[i : i + 39])
