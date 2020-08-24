cells = input("Enter cells:")
i = 0
lits = [["| ", cells[i], cells[i + 1], cells[i + 2], " |"] for i in range(len(cells)) if i % 3 == 0]
print("---------")
for i in range(len(cells)):
    if i % 3 == 0:
        print("| " + cells[i] + " " + cells[i + 1] + " " + cells[i + 2] + " |")
print("---------")
if (lits[0][0] == lits [0][1] or  '_') and (lits[0][1] == lits[0][2] or '_'):



