hearlist = set()
seelist = set()
n, m = map(int,input().split())
for i in range(n):
    hearlist.add(input())
for i in range(m):
    seelist.add(input())
deutbo = sorted(hearlist & seelist)
print (len(deutbo),*deutbo,sep = "\n")