import sys
apply_student = {}
input = sys.stdin.readline
jw, trm = map(int,input().split())
for i in range(0, trm):
    temp = input()
    if temp in apply_student:
        del apply_student[temp]
        apply_student[temp] = 1
    else:
        apply_student[temp] = 1
for key in apply_student:
    if jw >= 1:
        print(key, end="")
        jw -=1
    if jw == 0:
        break