n =int(input())
a = list(map(int,(input().split())))
b,c = map(int,input().split())
result = 0
for i in range(0, n):
    temp = int(a[i])
    result += 1
    temp -= b
    if temp > 0:
        result += (temp +c -1) // c
print(result)






#시간초과
"""n =int(input())
a = list(map(int,(input().split())))
b,c = map(int,input().split())
result = 0
for i in range(0, n):
    temp = int(a[i])
    if temp - b > 0:
        result += 1
        temp -= b
    while temp !=0:
        if temp - c > 0:
            result += 1
            temp -= c
        else:
            result += 1
            break
print(result)"""