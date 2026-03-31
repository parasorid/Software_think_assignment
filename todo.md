8958 난이도 미해결
3052

# 뭔진 모르겠지만 일단 짜고있던거임
hrepeat = int(input())
for k in range(0, hrepeat):
    score = list(input().split())
    sum = 0
    people = 0
    result = []
    ave = float()
    for i in range(1, len(score)):
        sum += int(score[i])
    ave = sum / int(score[0])
    for i in range(1, len(score)):
        if int(score[i]) > ave:
            people += 1
    result.append(float(people / int(score[0])))
for i in range(0, hrepeat):
    print("{:.3%}".format(result[i]))