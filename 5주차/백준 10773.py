forsum = []
for i in range(0, int(input())):
    n = int(input())
    if n != 0: forsum.append(n)
    else: del forsum[len(forsum)-1]
print(sum(forsum))