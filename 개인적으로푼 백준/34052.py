sum = 0
for i in range(0, 4):
    sum+= int(input())
if 1800 - sum >= 300:
    print("Yes")
else:
    print("No")