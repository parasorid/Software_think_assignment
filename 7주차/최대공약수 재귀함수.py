def maxsu(a, b):
    if b == 0:
        return a
    else:
        return maxsu(b, a%b)
a, b = map(int, input().split())
print("입력받은 두 수의 최대 공약수는", maxsu(a,b), "입니다")