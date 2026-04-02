# 값이 4개가 주어졌을떄, 가로 세로가 가능해야해
num4 = list(map(int,input().split()))
num4.sort()
print(num4[2]*num4[0])