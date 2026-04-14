s, n, m = map(int,input().split())
maxulist = s
size = 0
for i in range(0, n+m):
    temp = int(input())
    if temp == 1:
        if maxulist == size:
            size += 1
            maxulist *=2
        else:
            size += 1
    else:
        size -= 1
print(maxulist)