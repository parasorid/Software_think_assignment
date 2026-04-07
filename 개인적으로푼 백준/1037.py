n = int(input())
yaksu = list(map(int, input().split()))
if n == 1:
    print(yaksu[0]*yaksu[0])
    exit()
print(max(yaksu)*min(yaksu))