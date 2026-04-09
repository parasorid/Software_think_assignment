import math
def isprime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return(int(0))
    return(n)
n = int(input())
m = int(input())
m, n = int(max(m, n)), int(min(m, n))
primelist = []
if n <= 1:
    n = int(2)
for k in range(n, m+1):
    if isprime(k) == k:
        primelist.append(k)
if len(primelist) <= 0:
    print(-1)
else: print(sum(primelist),"\n", min(primelist), sep="")
