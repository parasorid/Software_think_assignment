def dsum(n):
    return n + sum(map(int,str(n)))
n = set()
for i in range(0, 10000):
    n.add(dsum(i))
for i in range(0, 10000):
    if i not in n:
        print(i)