t = int(input())
forprint = []
temp = str()
for i in range(0, t):
    userinput= list(input())
    for j in range(2, len(userinput)):
        temp += userinput[j] * int(userinput[0])
    forprint.append(temp)
    temp = str()
for i in range(0, len(forprint)):
    print(forprint[i])