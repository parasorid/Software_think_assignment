howmany = int(input())# 몇번이나 할건데?
sum = []
for i in range(0, howmany):
    a, b = map(int, input().split())
    sum.append(a+b)
for i in range(0, howmany):
    print(sum[i])