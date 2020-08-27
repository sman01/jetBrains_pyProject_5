sent = input().split()
li = [x for x in sent if x.endswith('s') is True]
print("_".join(li))
