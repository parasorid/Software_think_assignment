allsum = []
n = int(input())
for i in range(0, n):
    array = list(input())
    sum = 0
    streak = 0
    befnum = 0
    for i in range(0, len(array)):
        if array[i] == "O":
            streak += 1
            sum += streak
        else:
            streak = 0
    allsum.append(sum)
for i in range(0, n):
    print(allsum[i])