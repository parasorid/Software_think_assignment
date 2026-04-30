m = int(input())
date = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_day = sum(date[:m-1]) % 7
print('Su Mo Tu We Th Fr Sa')
print("    " * start_day, end="")
for day in range(1, date[m-1] + 1):
    print(f"{day:2}", end=" ")
    if (start_day + day) % 7 == 0:
        print()
print() # 마지막 줄바꿈