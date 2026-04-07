n = int(input())
sghas = list(map(int,input().split()))
m = int(input())
sgenl = list(map(int,input().split()))
sgn = {}
for nu in sghas:
    if nu in sgn:
        sgn[nu] += 1
    else:
        sgn[nu] = 1
for nu in sgenl:
    print(sgn.get(nu, 0), end = " ")



"""n = int(input())
sghas = list(map(int,input().split()))
m = int(input())
sgenl = list(map(int,input().split()))
forprint = []
for i in range(0, m):
    forprint.append(sghas.count(sgenl[i]))
for j in range(0, len(forprint)):
    print(forprint[j], end=" ")
"""