def datedecide(m):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m == 2:
        return 28
    else:
        return 30
#date = datedecide(m)


# 1월 1일이 일요일, #윤년이 아닌 해
# 요일 이름 목록
# 각 월의 시작요일 0,
#리스트로 각월이 얼마인지 정하기
#date = [31,28,31,30,31,30,31,31,30,31,30,31]

m = int(input())
date = [31,28,31,30,31,30,31,31,30,31,30,31]
m_date = date[m-1]

if m == 1:
    start_day = 0

else:
    for i in range(m):
        start_day += date[i]

if start_day != 0:
    start_day = start_day % 7

print('Sun','Mon','Tue','Wed','Tue','Fri','Sat', end= " ")

printday = 1
#출력단계
for i in range(0, start_day):
    print(" ", end = "")
for i in range(start_day, 7):
    print(printday)
    printday += 1
print("\n")
while True:
    if m_date +1 == printday:
        break
    for i in range(7, m_date+1):
        print(i, end = " ")
        printday +=1
