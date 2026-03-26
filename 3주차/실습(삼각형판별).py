A, B, C = map(int, input().split())

if A**2 + B**2 == C**2:
    print("직각 삼각형입니다.")
elif A**2 + B**2 > C**2:
    print("둔각 삼각형입니다.")
else:
    print("예각 삼각형입니다.")