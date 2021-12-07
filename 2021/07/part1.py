from statistics import median


def read_crabs():
    with open("crabs.txt") as f:
        return list(map(int, f.read().strip().split(",")))


def fuel_consumption(crabs, median):
    return sum([abs(crab - median) for crab in crabs])


if __name__ == "__main__":
    crabs = read_crabs()
    median = round(median(crabs))
    fuel = fuel_consumption(crabs, median)
    print(f"total crab submarine fuel consumption is {fuel}")
