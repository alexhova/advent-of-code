from part1 import read_bingo, mark_board, bingo

numbers, boards = read_bingo()
for number in numbers:
    for board in boards:
        mark_board(board, number)
        if bingo(board):
            board["bingos"] += 1
            least_bingos = sorted(boards, key=lambda k: k["bingos"])[0]["bingos"]
            if least_bingos == 1:
                score = sum([int(n) for n in board["unmarked"]]) * int(number)
                exit(f"loser! score is {score}")
