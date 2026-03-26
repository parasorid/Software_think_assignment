import math
sentence = input()
sum = 0
for i in range(0, len(sentence)):
    if 'a'<=sentence[i] <= 'z' :
        sum+= ord(sentence[i]) - 96
    else:
        sum +=ord(sentence[i]) - 38

for i in range(2, int(math.sqrt(sum))+ 1):
    if sum % i == 0:
        print("It is not a prime word.")
        break
else:
    print("It is a prime word.")