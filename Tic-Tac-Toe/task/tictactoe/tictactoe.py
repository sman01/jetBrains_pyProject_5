import numpy as np
x_cord, y_cord = 0, 0


def checkwin():
    if m[0][0] == m[1][1] == m[2][2] == "X" or m[0][2] == m[1][1] == m[2][0] == "X":
        print("X wins")
    elif m[0][0] == m[1][1] == m[2][2] == "O" or m[0][2] == m[1][1] == m[2][0] == "O":
        print("O wins")
    elif m[0][0] == m[0][1] == m[0][2] == "X" or m[1][0] == m[1][1] == m[1][2] == "X" or m[2][0] == m[2][1] == m[2][2] == "X":
        print("X wins")
    elif m[0][0] == m[1][0] == m[2][0] == "X" or m[0][1] == m[1][1] == m[2][1] == "X" or m[0][2] == m[1][2] == m[2][2] == "X":
        print("X wins")
    elif m[0][0] == m[0][1] == m[0][2] == "O" or m[1][0] == m[1][1] == m[1][2] == "O" or m[2][0] == m[2][1] == m[2][2] == "O":
        print("O wins")
    elif m[0][0] == m[1][0] == m[2][0] == "O" or m[0][1] == m[1][1] == m[2][1] == "O" or m[0][2] == m[1][2] == m[2][2] == "O":
        print("O wins")
    else:
        print('oo')
        checip()


def checip():
    x, y = input("Enter the coordinates:").split()
    global x_cord, y_cord
    if x.isdecimal() and y.isdecimal():
        xf = int(x)
        yf = int(y)
        if xf <= 3 and yf <= 3:
            x_cord = xf - 1
            y_cord = yf - 1
            global i
            i += 1
        elif xf > 3 or yf > 3:
            print("Coordinates should be from 1 to 3!")
            checip()
    else:
        print("You should enter numbers!")
        checip()


m = np.full((3, 3), "_")


def matcheck():
    global m
    global i
    if m[abs(2 - y_cord)][x_cord] != "_":
        print("ye")
        if i % 2 == 0:
            m[abs(2 - y_cord)][x_cord] = "O"
        else:
            m[abs(2 - y_cord)][x_cord] = "X"
        checkwin()

    else:
        print("This cell is occupied! Choose another one!")
        checip()
        checkwin()


print("---------")
for i in range(3):
    print(f'|       |')
print("---------")
i = 0

for j in range(9):
    print("---------")
    for i in range(3):
        print(f'| {m[i][0]} {m[i][1]} {m[i][2]} |')
    print("---------")
    checip()
