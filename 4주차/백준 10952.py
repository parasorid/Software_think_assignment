a, b = 9, 9
sum = []
while a != 0 and b != 0:
    a, b = map(int, input().split())
    if a+b==0:
        break
    sum.append(a+b)
for i in range(0, len(sum)):
    print(sum[i])