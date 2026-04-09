sum = 0
def istdeungcha(n):
    templ =list(map(int,str(n)))
    tempb = templ[0] - templ[1]
    for i in range(1, len(templ)-1):
        if tempb == templ[i] - templ[i+1]:
            tempb = templ[i] - templ[i+1]
        else:
            return(0)
    return(1)
n = int(input())
if n < 100:
    print(n)
    exit()
for i in range(100, n+1):
    sum +=istdeungcha(i)
print(sum+99)