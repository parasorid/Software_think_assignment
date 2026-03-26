import datetime

now= datetime.datetime.now()

if 3<= now.month <= 5:
    print("예쁜 벚꽃잎이 흩날리는 {Month}월의 봄입니다.".format(Month=now.month))
if 6<= now.month <= 8:
    print("뜨거운 햇빛이 세상을 데우는 {Month}월의 여름입니다.".format(Month=now.month))
if 9<= now.month <= 11:
    print("세상이 천천히 갈색으로 물들어가는 {Month}월의 가을입니다.".format(Month=now.month))
if 12<= now.month <= 2:
    print("새하얗게 덮여 호- 불면 입김이 보이는 {Month}월의 겨울입니다.".format(Month=now.month))