if __name__ == "__main__":
    position = 0
    depth = 0
    aim = 0

    with open("commands.txt") as f:
        for command in f:
            direction, magnitude = command.split(" ")
            magnitude = int(magnitude)

            if direction == "down":
                aim += magnitude
            elif direction == "up":
                aim -= magnitude    
            elif direction == "forward":
                position += magnitude
                depth += aim * magnitude

    print(f"final position is {position*depth}")
