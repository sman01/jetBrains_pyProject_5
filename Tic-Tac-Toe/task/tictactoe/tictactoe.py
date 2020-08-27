import numpy as np
import math
Xwin = 0
Owin = 0
Xcount = 0
Ocount = 0
blankcount = 0
layout = input("Enter cells:")
for x in layout:
    if x == "X":
        Xcount += 1
    elif x == "O":
        Ocount += 1
    elif x == "_":
        blankcount += 1
lay = np.array([x for x in layout])
m = lay.reshape(3, 3)
print("---------")
for i in range(3):
    print(f'| {m[i][0]} {m[i][1]} {m[i][2]} |')
print("---------")
if m[0][0] == "X" and m[1][1] == "X" and m[2][2] == "X":
    Xwin += 1
if m[0][0] == "O" and m[1][1] == "O" and m[1][1] == "O":
    Owin += 1
if m[0][2] == "X" and m[1][1] == "X" and m[2][0] == "X":
    Xwin += 1
if m[0][2] == "O" and m[1][1] == "O" and m[2][0] == "O":
    Owin += 1
for i in range(3):
    strlineX = 0
    strlineO = 0
    if m[0][i] == m[1][i] == m[2][i] == "X":
        Xwin += 1
    elif m[0][i] == m[1][i] == m[2][i] == "O":
        Owin += 1
    elif m[i][0] == m[i][1] == m[i][2] == "X":
        Xwin += 1
    elif m[i][0] == m[i][1] == m[i][2] == ")":
        Owin += 1


if abs((Xcount - Ocount)) > 1:
    print("Impossible")
elif abs(Xwin - Owin) > 1:
    print("Impossible")
elif Xwin == 1 and Owin == 1:
    print("Impossible")
else:
    if Xwin >= 1:
        print("X wins")
    elif Owin >= 1:
        print("O wins")
    elif "_" in layout:
        print("Game not finished")
    else:
        print("Draw")
