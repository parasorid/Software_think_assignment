h, m = map(int, input().split())
wtw = h*60 + m - 45
if wtw < 0:
    wtw= wtw+1440
print(wtw//60, wtw%60)