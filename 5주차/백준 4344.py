repeatn = int(input())
allnum = []
tempsum = 0
tempresult = 0
printresult = []
temp = 0
for i in range (0, repeatn):
    allnum.append(list(map(int, (input().split()))))
for i in range(0, repeatn):
    tempsum = sum(allnum[i][1:])
    tempresult = tempsum / allnum[i][0]
    for k in range(1, len(allnum[i])):
        if allnum[i][k] > tempresult :
            temp += 1
    printresult = temp/int(allnum[i][0])
    print(f"{printresult:.3%}")
    temp, tempresult, tempsum = 0,0,0