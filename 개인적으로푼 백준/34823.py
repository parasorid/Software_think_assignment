y, c, p = map(int,input().split())
print(min(y, min(c // 2, p)))


"""ycpc = 0
y, c, p = map(int,input().split())
for i in range (0, max(y,c,p)):
    if y>= 1 and c>= 2 and p >=1:
        y, c, p = y-1, c-2, p-1
        ycpc += 1
    else:
        break
print(ycpc)"""