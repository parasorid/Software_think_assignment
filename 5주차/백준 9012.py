forcheck = []
result = []
nvpp = 0
for i in range(0, int(input())):
    forcheck = list(input())
    for j in range(0, len(forcheck)):
        if forcheck[j] == "(":
            nvpp += 1
        else:
            nvpp -= 1
        if nvpp < 0:
            break
    if nvpp == 0:
        result.append("YES")
    else:
        result.append("NO")
    nvpp = 0
for i in range(0, len(result)):
    print(result[i])




"""
forcheck = []
result = []
for i in range(0, int(input())):
    forcheck = list(input())
    if forcheck.count("(") != forcheck.count(")"): result.append("NO")
    else: result.append("YES")
for i in range(0, len(result)):
    print(result[i])
"""