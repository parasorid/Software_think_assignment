import string
ulist = input()
ulist = ulist.lower()
ulist = list(ulist)
ulist.sort()
forresult = []
for i in range(0, 26):
    temp = ulist.count(string.ascii_lowercase[i])
    forresult.append(temp)
if int(forresult.count(max(forresult))) > 1:
    print("?")
else:
    print(string.ascii_uppercase[forresult.index(max(forresult))])