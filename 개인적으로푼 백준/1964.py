sum = 0
n = int(input())
if n == 1:
    sum = 5
else:
    for i in range(2, n+1):
        sum += (i* 3) +1
    sum += 5
print(sum % 45678)