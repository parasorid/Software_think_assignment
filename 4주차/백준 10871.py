n, x = map(int, input().split())
array = list(map(int, (input().split())))
for i in range(0, n):
    if array[i] < x:
        print(array[i], end= ' ')
