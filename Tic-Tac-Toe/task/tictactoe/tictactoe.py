cells = input("Enter cells:")
i = 0
print("---------")
for i in range(len(cells)):
    if i % 3 == 0:
        print("| " + cells[i] + " " + cells[i + 1] + " " + cells[i + 2] + " |")
print("---------")
