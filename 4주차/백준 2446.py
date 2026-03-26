xy = int(input())
for i in range(0, xy):
    print(" " * i + "*" * (2*xy-1 - 2* i))
for i in range(xy-2, -1, -1):
    print(" " * i + "*" * (2*xy-1 - 2* i))