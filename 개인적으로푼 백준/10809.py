apbdict = {}
import string
userinput = list(input())
for i in range(0, 26):
    if string.ascii_lowercase[i] in userinput:
        apbdict[string.ascii_lowercase[i]] =userinput.index(string.ascii_lowercase[i])
    else:
        apbdict[string.ascii_lowercase[i]] = -1
for i in range(0,26):
    print(apbdict[string.ascii_lowercase[i]], end = " ")