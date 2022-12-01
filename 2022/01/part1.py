def read_calories() -> str:
    with open("calories.txt") as f:
        return f.read()


def max_calories(calories: str) -> int:
    return max(sum(map(int, c.strip().split("\n"))) for c in calories.split("\n\n"))


if __name__ == "__main__":
    calories = read_calories()
    most_calories = max_calories(calories)
    print(f"the elf with the most calories is carrying {most_calories} calories")
