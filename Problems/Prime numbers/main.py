prime_numbers = []
for i in range(2, 1001):
    boolean = [i for j in range(2, i-1) if i % j == 0]
    if any(boolean):
        continue
    else:
        prime_numbers.append(i)




