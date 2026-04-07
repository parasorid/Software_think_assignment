#n이 주어졌을 때 n 까지의 모든 소수를 출력하라
import math
n = int(input())
temp = 0
if n <= 0:
    print("0 이하의 수로는 소수를 구할 수 없습니다.")
    exit()
istprime = [True] * (n+1)
istprime[0], istprime[1] = False, False
for i in range(2, int(math.sqrt(n)+1)):
    if istprime[i]:
        for j in range(i*i, n+1, i):
            istprime[j] = False
for i in range(2, n+1):
    if istprime[i]:
        print(i)