soldbook = []
soldbookl = []
soldbookc = []
for i in range(int(input())):
    soldbook.append(input())
soldbookl = list(set(soldbook))
soldbookl.sort()
for j in range(len(soldbookl)):
    soldbookc.append(soldbook.count(soldbookl[j]))
print(soldbookl[soldbookc.index(max(soldbookc))])

# soldbookc에서 맥스인것의 위치를 찾은 다음에 그걸 soldbook l에서 불러와야함