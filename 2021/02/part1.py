position = 0
depth = 0

with open("commands.txt") as f:
    for command in f:
        direction, magnitude = command.split(" ")
        magnitude = int(magnitude)

        if direction == "down":
            depth += magnitude
        elif direction == "up":
            depth -= magnitude
        elif direction == "forward":
            position += magnitude

print(f"final position is {position*depth}")
