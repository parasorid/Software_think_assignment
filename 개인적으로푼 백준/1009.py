# 백준 1009
a = int(input())
result = []
for i in range(0, a):
    x, y = map(int,input().split())
    result.append(pow(x, y, 10))
for i in range(0, a):
    needp = int(result[i])
    if needp == 0:
        print("10")
    else:
        print(needp)