trynum = int(input())
sum = []
for i in range(0, trynum):
    a, b = map(int,input().split())
    sum.append(a+b)
for i in range(0, trynum):
    print("Case #{}: {}".format(i+1, sum[i]))
