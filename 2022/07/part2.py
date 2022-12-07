from part1 import read_commands, parse_line

if __name__ == "__main__":
    commands = read_commands()
    pwd = "/"
    dir_sizes = {}

    for line in commands:
        pwd, dir_sizes = parse_line(pwd, dir_sizes, line)

    space_needed = 30000000 - (70000000 - dir_sizes["/"])
    for size in sorted(dir_sizes.values()):
        if size > space_needed:
            print(f"delete directory with size {size}")
            break
