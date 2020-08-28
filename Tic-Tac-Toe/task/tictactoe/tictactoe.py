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


def checip():
    x, y = input("Enter the coordinates:").split()
    global x_cord, y_cord
    if x.isdecimal() and y.isdecimal():
        xf = int(x)
        yf = int(y)
        if xf <= 3 and yf <= 3:
            x_cord = xf - 1
            y_cord = yf - 1
            matcheck()
        elif xf > 3 or yf > 3:
            print("Coordinates should be from 1 to 3!")
            checip()
    else:
        print("You should enter numbers!")
        checip()


layout = input("Enter cells:")
layout = layout.replace("_", " ")
lay = np.array([x for x in layout])
m = lay.reshape(3, 3)


def matcheck():
    global m
    if m[abs(2 - y_cord)][x_cord] != ' ':
        print("This cell is occupied! Choose another one!")
        checip()
    else:
        m[abs(2 - y_cord)][x_cord] = "X"


print("---------")
for i in range(3):
    print(f'| {m[i][0]} {m[i][1]} {m[i][2]} |')
print("---------")
checip()
print("---------")
for i in range(3):
    print(f'| {m[i][0]} {m[i][1]} {m[i][2]} |')
print("---------")
