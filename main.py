n = int(input())
result = 0
befsum = 0
uinput = list(map(int,input().split()))
uinput.sort()
for i in range(0, n):
    result += uinput[i] * i - befsum
    befsum += uinput[i]
print(2 * result)