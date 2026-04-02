n = int(input())
summary = 0
for i in range(0, n):
    a = list(map(int,input().split()))
    summary += sum(a)
print(summary)