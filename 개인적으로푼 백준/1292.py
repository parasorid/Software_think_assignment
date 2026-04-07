origin = 1
resultlist = []
while len(resultlist) <= 1000:
    for i in range(origin):
        resultlist.append(origin)
    origin += 1
a, b = map(int,input().split())
print (sum(resultlist[a-1:b]))