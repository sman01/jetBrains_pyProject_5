pas = input().split()
ct = 0
for p in pas:
    if p == "A":
        ct += 1
print(round(ct/len(pas), 2))
