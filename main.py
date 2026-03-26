array = []
for i in range(0,9):
    array.append(int(input()))
print(max(array), array.index(max(array))+1,sep=" ")