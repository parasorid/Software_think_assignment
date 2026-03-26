# origin, hope, percent = 100, 200, 5
balance = 1000000
year = 0
while balance <= 2000000:
    balance *= 1.05
    year += 1
print("귀하가 {}년 간 예금하시는 경우 {}원을 최종적으로 수령받으실 수 있습니다.".format(year, int(balance)))