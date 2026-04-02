#셀프 코딩
""""
userinput = []
divided = []
available = 0
for i in range(0, 10):
    userinput.append(int(input()))
for i in range(0, 10):
    if int(userinput[i]) % 42 not in divided:
        available += 1
    divided.append(userinput[i] % 42)
print(available)
"""