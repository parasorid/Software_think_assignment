n = int(input())
result = 0
befsum = 0
uinput = list(map(int,input().split()))
uinput.sort()
for i in range(0, n):
    result += uinput[i] * i - befsum
    befsum += uinput[i]
print(2 * result)

# 핵심 구조는 누적합,
# 또한 정렬되어있으므로 언제나 큰값에서 작은값을 뺄 수 있고
# 원소 [1, 2, 3] 이 있을때 3-1 + 3-2 = 3 이기도 하나
# 3 * 2(3의 원소번호) - 2 1 (누적합)
#이기도 하므로, 해당 부분을 잘 기억해보자.