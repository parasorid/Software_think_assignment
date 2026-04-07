#영식요금제는 30초마다 10원씩, 민식요금제는 60초마다 15원
ys = 0
ms = 0
n = int(input())
t_time = list(map(int,input().split()))
for i in range(0, n):
    ys += (t_time[i] // 30 + 1) *10
    ms += (t_time[i]// 60 + 1) *15
if ys == ms:
    print("Y M", ys, sep = " ")
elif ys >= ms:
    print("M", ms, sep = " ")
else:
    print("Y", ys, sep =" ")