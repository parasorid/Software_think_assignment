nlist = []
for i in range(0, 30):
    nlist.append(i+1)
for i in range(28):
        te = int(input())
        if te in nlist:
            nlist.remove(te)
print(min(nlist), max(nlist), sep = "\n")