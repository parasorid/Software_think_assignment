yut1 = list(map(int, input().split()))
yut2 = list(map(int, input().split()))
yut3 = list(map(int, input().split()))
yut1_sum = 0
yut2_sum = 0
yut3_sum = 0

for i in range(4):
    yut1_sum += yut1[i]
for i in range(4):
    yut2_sum += yut2[i]
for i in range(4):
    yut3_sum += yut3[i]

if yut1_sum == 0:
        print("D")
elif yut1_sum ==1:
        print("C")
elif yut1_sum ==2:
        print("B")
elif yut1_sum ==3:
        print("A")
else:
        print("E")

if yut2_sum == 0:
        print("D")
elif yut2_sum ==1:
        print("C")
elif yut2_sum ==2:
        print("B")
elif yut2_sum ==3:
        print("A")
else:
        print("E")

if yut3_sum == 0:
        print("D")
elif yut3_sum ==1:
        print("C")
elif yut3_sum ==2:
        print("B")
elif yut3_sum ==3:
        print("A")
else:
        print("E")