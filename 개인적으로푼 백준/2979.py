def carintime(ts, te):
    temp = []
    for i in range(ts, te):
        temp.append(i)
    return temp

allcar = []
result = 0
pa, pb, pc = map(int,input().split())
for i in range(0, 3):
    ts, te = map(int,input().split())
    allcar += carintime(ts,te)
for i in range(1, max(allcar)+1):
    temp = allcar.count(i)
    if temp == 1 :
        result += pa
    elif temp == 2 :
        result += pb*2
    elif temp == 3 :
        result += pc *3
print(result)