def print_table():
    print(f"---------\n"
          f"| {i_cells[0][0]} {i_cells[0][1]} {i_cells[0][2]} |\n"
          f"| {i_cells[1][0]} {i_cells[1][1]} {i_cells[1][2]} |\n"
          f"| {i_cells[2][0]} {i_cells[2][1]} {i_cells[2][2]} |\n"
          f"---------")


cells = "         "
i_cells = [[cells[0], cells[1], cells[2]], [cells[3], cells[4], cells[5]], [cells[6], cells[7], cells[8]]]
turn, messx, messo, imp = "X", "", "", 0
print_table()
while True:
    if (["X", "X", "X"] in i_cells) or (i_cells[0][0] == "X" and i_cells[1][1] == "X" and i_cells[2][2] == "X") or \
            (i_cells[0][2] == "X" and i_cells[1][1] == "X" and i_cells[2][0] == "X"):
        print("X wins")
        break
    elif (["O", "O", "O"] in i_cells) or (i_cells[0][0] == "O" and i_cells[1][1] == "O" and i_cells[2][2] == "O") or \
            (i_cells[0][2] == "O" and i_cells[1][1] == "O" and i_cells[2][0] == "O"):
        print("O wins")
        break
    elif i_cells[0].count(" ") + i_cells[1].count(" ") + i_cells[2].count(" ") == 0:
        print("Draw")
        break
    else:
        x = input("Enter the coordinates: ").split()

    if x[0] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        print("You should enter numbers!")
        continue

    x, y = int(x[0]), int(x[1])

    if x not in range(4) or y not in range(4):
        print("Coordinates should be from 1 to 3!")
    elif i_cells[abs(y - 3)][x - 1] != " ":
        print("This cell is occupied! Choose another one!")
    elif turn == "X":
        turn = "O"
        i_cells[abs(y - 3)][x - 1] = "X"
    else:
        turn = "X"
        i_cells[abs(y - 3)][x - 1] = "O"

    print_table()
