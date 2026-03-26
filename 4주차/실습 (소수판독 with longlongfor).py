# 시간과 관련된 기능을 가져옵니다.
import time
n = int(input("자연수 > "))
# 소수를 구하기전 시간을 저장 합니다.
start_time = time.time()
# 코드를 원하는대로 실컷 써내려보자
for i in range(2, n):
    if n % i == 0:
        print("귀하가 입력하신수 {}는 자기 자신과 1 이외 {}로도 나누어짐을 확인하였습니다. 그러므로 소수가 아닙니다.".format(n, i))
        break
else:
    print("귀하가 입력하신 수 {}는 소수입니다.".format(n))


# 걸린 시간을 출력합니다.
print("걸린 시간 :", time.time() - start_time)