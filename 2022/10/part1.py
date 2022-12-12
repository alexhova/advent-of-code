def read_signals(filename):
    with open(filename) as f:
        return f.read().splitlines()


def check_cycle(x, cycle):
    if cycle in [20, 60, 100, 140, 180, 220]:
        return x * cycle
    return 0


if __name__ == "__main__":
    signals = read_signals("signals.txt")
    x = 1
    cycle = 0
    signal_strength = 0

    for signal in signals:
        cycle += 1
        signal_strength += check_cycle(x, cycle)
        if signal.split(" ")[0] == "addx":
            cycle += 1
            signal_strength += check_cycle(x, cycle)
            x += int(signal.split(" ")[1])

    print("the total signal strength is", signal_strength)
