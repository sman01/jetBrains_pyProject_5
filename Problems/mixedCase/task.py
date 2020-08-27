sent = input().split(' ')

if len(sent) > 1:
    for i in range(1, len(sent)):
        x = sent[i]
        sent[i] = x.capitalize()
print("".join(sent))
