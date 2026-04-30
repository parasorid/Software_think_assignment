import random
def gscal(n): #1
    rl = []
    tl = []
    A, B, C = gsmaker(n),gsmaker(n),gsmaker(n)
    for i in range(n):
        tl = []
        for j in range(n):
            tn = 0
            for k in range(n):
                tn += A[i][k] * B[k][j]
            tl.append(tn+C[i][j])
        rl.append(tl)
    return rl
def gsts(n, nlist): #2
    tl = []
    rl = []
    for i in range(n):
        tl = []
        for j in range(n):
            tl.append(nlist[j][i])
        rl.append(tl)
    return rl
def gsmaker(n): #3
    ttl = []
    tl = []
    for i in range(n):
        ttl = []
        for j in range(n):
            ttl.append(random.randrange(1, n*n*10))
        tl.append(ttl)
    return tl
def gsprint(n, tlist): #4
    for i in range(n):
        for j in range(n):
            print(f"{tlist[i][j]:7d}", end = " ")
        print()

nnlist= []
while True:
    print("먼저 당사의 프로그램을 이용해주셔서 감사합니다. 아래의 코드 중 원하는 것을 입력해 주십시오.","0: 프로그램 종료", "1: 행렬 생성", "2: 행렬 연산 (A*B+C)", "3. 전치행렬", sep="\n")
    temp = input()
    if 0 == int(temp):
        print("프로그램이 종료됩니다. 당사의 프로그램을 이용해주셔서 감사드립니다.")
        break
    elif 1 == int(temp):
        print("귀하께서는 행렬 생성을 선택해주셨습니다.", "1부터 5 사이의 정수를 입력해주십시오.", sep = "\n")
        n = int(input())
        if n >= 1 or n < 6:
            gsprint(n, gsmaker(n))
        else:
            print("범위외의 정수가 입력되었습니다. 처음으로 돌아갑니다.")
            break
    elif 2 == int(temp):
        print("귀하께서는 행렬 연산을 선택해주셨습니다.", "1부터 5 사이의 정수를 입력해주십시오.", sep = "\n")
        n = int(input())
        if n >= 1 or n < 6:
            gsprint(n,gscal(n))
        else:
            print("범위외의 정수가 입력되었습니다. 처음으로 돌아갑니다.")
            break
    elif 3 == int(temp):
        print("귀하께서는 전치행렬을 선택해주셨습니다.", "1부터 5 사이의 정수를 입력해주십시오.", sep = "\n")
        n = int(input())
        if n >= 1 or n < 6:
            gsts(n, gsmaker(n))
        else:
            print("범위외의 정수가 입력되었습니다. 처음으로 돌아갑니다.")
            break