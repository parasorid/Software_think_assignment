import sys
input = sys.stdin.readline
repeatn = int(input())
nlist = list()
for i in range(0, repeatn):
    nlist.append(int(input()))
nlist.sort()
for i in range(0, repeatn):
    print(nlist[i])