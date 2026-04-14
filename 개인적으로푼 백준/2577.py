sum = int(input())
for i in range(2):
    sum *= int(input())
result = list(str(sum))
for i in range(0, 10):
    print(result.count(str(i)))