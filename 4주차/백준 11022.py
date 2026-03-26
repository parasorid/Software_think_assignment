trynum = int(input())
a = []
b = []
for i in range(0, trynum):
    x, y = map(int,input().split())
    a.append(x)
    b.append(y)
for i in range(0, trynum):
    print("Case #{}: {} + {} = {}".format(i+1, a[i], b[i], a[i]+b[i]))