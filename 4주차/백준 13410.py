x,y = map(int,input().split())
sum = []
for i in range(1, y+1):
    temp = x*i
    sum.append(int(str(temp)[::-1]))
print(max(sum))