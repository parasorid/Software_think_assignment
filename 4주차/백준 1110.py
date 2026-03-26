original, current, cycle, sumn, a, b = 0, -1, 0, 0, 0, 0
original = int(input())
a, b = (original //10) %10, original %10
while original != int(current):
    cycle += 1
    sumn= a+b
    current = str(b)+str(sumn % 10)
    a, b = (int(current) //10) %10, int(current) %10

print(cycle)





"""
resultnumber = 0
cycle = 0
number = input()
if int(number) < 10:
    number = str("0" + number)
a, b = list(map(int, str(number)))
print(number, a, b)
while int(number) != int(resultnumber):0
    cycle += 1?
    sumnumb = a+b
    d= (sumnumb)%10
    resultnumber = str(b + d)
    if sumnumb < 10:
       sumnumb = str("0" + str(sumnumb))
    a, b=list(map(int, str(sumnumb)))
print(cycle)
"""