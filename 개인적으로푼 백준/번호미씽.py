n = int(input())
n*=n
if n  <=100000000:
    print("Accepted")
else:
    print("Time limit exceeded")


    rst=0
n = int(input())
cslist = list(map(int,input().split()))
cslist.sort()
for i in range(0, n+1):
    rst+=int(sum(cslist[:i]))
print(rst)