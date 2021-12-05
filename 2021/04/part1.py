def read_bingo():
    with open("bingo.txt") as f:
        numbers = f.readline().strip().split(",")
        boards = []
        for line in f:
            if not line.strip():
                boards.append(make_board(f))
    return numbers, boards


def make_board(f):
    board = {"unmarked": [], "rows": [], "cols": [[], [], [], [], []], "bingos": 0}
    for _ in range(5):
        row = [n.strip() for n in f.readline().split(" ") if n]
        board["unmarked"].extend(row)
        board["rows"].append(row)
        for i, n in enumerate(row):
            board["cols"][i].append(n)
    return board


def mark_board(board, number):
    if number not in board["unmarked"]:
        return
    board["unmarked"].remove(number)
    [row.remove(number) for row in board["rows"] if number in row]
    [col.remove(number) for col in board["cols"] if number in col]


def bingo(board):
    if [] in board["rows"] or [] in board["cols"]:
        return True


if __name__ == "__main__":
    numbers, boards = read_bingo()
    for number in numbers:
        for board in boards:
            mark_board(board, number)
            if bingo(board):
                score = sum([int(n) for n in board["unmarked"]]) * int(number)
                exit(f"bingo! score is {score}")
