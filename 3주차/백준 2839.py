# 상근 has 3, 5 kilo sugar 포대
# he wants less 포대
# 5로 나누고 그 나머지값을 기준으로 3으로 나눈 다음에 그게 0이 아니면 -1 출력
want = int(input())
if want % 3 == 0:
    print(want // 3)
else:
    for i in range(want // 5, 1, -1):
        notpackaged = want - (5 * i)
        if notpackaged % 3 == 0:
            print(notpackaged//3+i)
            break

    else:
     print("-1")