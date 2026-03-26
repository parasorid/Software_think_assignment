linen = int(input())
for i in range(linen, 0, -1):
    for j in range(1, i):
        print(" ", end= '')
    for k in range(i, linen+1):
        print("*", end='')
    print("")