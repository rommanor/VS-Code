size = int(input("Enter the size of the board: "))

board = []
for i in range(size):
    row = []
    for x in range(size):
        row.append("|-|")
    board.append(row)

def display_board():
    for row in board:
        print("".join(row))

display_board()