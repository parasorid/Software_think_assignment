#버블정렬을 구현하라
nlist = list(map(int, input().split())) # 유저가 구하고 싶은 정렬을 입력하세요
for i in range(len(nlist)): # 우리는 nlist의 총 원소 개수만큼 반복할거에요.
    for j in range(0, len(nlist)-1-i): # j는 0부터 len(nlist)- 1(보험용, 후에 하나 더해줄 예정에 있어서 오류 방지용) - i (맨 뒤 원소는 빼야하니까)
        if nlist[j] > nlist[j+1]: # 만약 j번에 있는 값이 그 뒷값보다 크면
            nlist[j], nlist[j+1] = nlist[j+1], nlist[j] # j번에 있는 값과 그 뒷값을 서로 스왑해주세용
print(nlist)





"""
#버블 정렬 구현해야하는데 내가 구현한건 선택정렬이래!
nlist = list(map(int, input().split()))
for i in range(len(nlist)-1, -1, -1):
    for j in range(0, i):
        if nlist[i] < nlist[j]:
            nlist[i], nlist[j] = nlist[j], nlist[i]
print(nlist)
"""