def read_commands():
    with open("commands.txt") as f:
        return f.read().splitlines()


def parse_line(
    pwd: str, dir_sizes: dict[str, int], line: str
) -> tuple[str, dict[str, int]]:
    if line.startswith("$ cd "):
        directory = line.split(" ")[-1]
        pwd = cd(pwd, directory)
    elif line[0].isnumeric():
        dir_sizes = add_file_size(pwd, dir_sizes, int(line.split(" ")[0]))
    return pwd, dir_sizes


def cd(pwd: str, directory: str) -> str:
    if directory == "/":
        pwd = "/"
    elif directory == "..":
        pwd = pwd.rsplit("/", 1)[0]
    else:
        pwd += f"/{directory}"
    return pwd


def add_file_size(
    pwd: str, dir_sizes: dict[str, int], file_size: int
) -> dict[int, str]:
    while pwd:
        dir_size = dir_sizes.get(pwd, 0)
        dir_sizes[pwd] = dir_size + file_size
        pwd = pwd.rsplit("/", 1)[0]
    return dir_sizes


if __name__ == "__main__":
    commands = read_commands()
    pwd = "/"
    dir_sizes = {}

    for line in commands:
        pwd, dir_sizes = parse_line(pwd, dir_sizes, line)

    total_size = 0
    for size in dir_sizes.values():
        if size < 100000:
            total_size += size

    print(f"total size of directories is {total_size}")
    print(dir_sizes)
