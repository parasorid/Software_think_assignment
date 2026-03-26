H, M, S = map(int, input().split())
plustime = int(input())
addedtime = 0

S = S+ plustime % 60
if S>=60:
    S-=60
    addedtime = 1
M = (M+addedtime) + plustime // 60 % 60
addedtime =0
if M>=60:
    M-=60
    addedtime = 1
H = (H+addedtime) + plustime // 3600 % 24
if H>=24:
    H-=24

print (H, M, S)