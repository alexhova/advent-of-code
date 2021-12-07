def read_lanternfish():
    with open("lanternfish.txt") as f:
        return [int(n) for n in f.read().strip().split(",")]


def advance(timers):
    new_timers = []
    for t in timers:
        new_timers.extend([6, 8]) if t == 0 else new_timers.append(t - 1)
    return new_timers


if __name__ == "__main__":
    timers = read_lanternfish()
    for _ in range(80):
        timers = advance(timers)
    print(f"lanternfish population after 80 days: {len(timers)}")
