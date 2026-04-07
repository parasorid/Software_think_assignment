userenterd = 1
forstore = []
is_work = True
templ= []
temp = 0
while is_work:
    userenterd = input()
    if int(userenterd) == 0:
        is_work = False
        break
    else:
        templ = list(userenterd)
        for i in range(0, len(templ)):
            if int(templ[i]) == 0:
                temp += 4
            elif int(templ[i]) == 1:
                temp += 2
            else:
                temp += 3
        temp += len(templ) +1
    forstore.append(int(temp))
    temp = 0
    templ = []
for i in range(0, len(forstore)):
    print(forstore[i])