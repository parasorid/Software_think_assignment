templist = []
printresult = []
while True:
    templist = input()
    if templist == "EOI":
        break
    templist = templist.lower()
    if "nemo" in templist:
        printresult.append("Found")
    else:
        printresult.append("Missing")
for i in range (len(printresult)):
    print(printresult[i])