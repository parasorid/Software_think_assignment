# 정수로 구성된 리스트에서 가장 작은 수
a = [8,4,9,5]
small = a[0]
for i in range(len(a)):
    if small >= a[i]: small = a[i]
print(small)