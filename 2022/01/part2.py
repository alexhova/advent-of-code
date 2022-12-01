from part1 import read_calories


def top_three_calories(calories: str) -> int:
    return sum(sorted(sum(map(int, c.strip().split("\n"))) for c in calories.split("\n\n"))[-3:])


if __name__ == "__main__":
    calories = read_calories()
    top_three = top_three_calories(calories)
    print(f"the three elves carrying the most calories have {top_three} calories total")
