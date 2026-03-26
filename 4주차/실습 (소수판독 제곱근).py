import math
# 시간과 관련된 기능을 가져옵니다.
import time
n = int(input("자연수 > "))
# 소수를 구하기전 시간을 저장 합니다.
start_time = time.time()
#코드써재껴보자고~
for i in range(2, int(math.sqrt(n)) + 1 ) :
    if n % i == 0:
        print("{N}은 {I}로 나누어 떨어집니다. 그러므로 소수가 아닙니다.".format(N= n, I= i))
        break
else:
    print("{}는 소수야.".format(n))

# 걸린 시간을 출력합니다.
print("걸린 시간 :", time.time() - start_time)