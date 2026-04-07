n = int(input())
ulist = []
rlist = list(input())
for i in range(0, n -1):
    ulist = list(input())
    for j in range(0, len(ulist)):
        if ulist[j] == rlist[j]:
            rlist[j] = ulist[j]
        else:
            rlist[j] = "?"
for k in range(len(rlist)): print(rlist[k], end= "")