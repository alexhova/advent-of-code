from statistics import mean
from part1 import read_crabs


def fuel_consumption(crabs, mean):
    fuel = 0
    for crab in crabs:
        steps = abs(crab - mean)
        fuel += (steps / 2) * (steps + 1)
    return int(fuel)


if __name__ == "__main__":
    crabs = read_crabs()
    means = int(mean(crabs)), int(mean(crabs) + 1)
    fuels = [fuel_consumption(crabs, mean) for mean in means]
    print(f"total crab submarine fuel consumption is {min(fuels)}")
