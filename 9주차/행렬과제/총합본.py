import random
import numpy as np
"""과제..
5월 7일 시험에는  N x N 행렬(리스트) 연산, 그리고 함수가 섞여 있는 문제를 낼 예정입니다.
5월 5일은 수업이 없는 대신, 다음의 과제를 하시면 됩니다.
    1보다 크고 5보다 작거나 같은 N을 입력받아
    1. N x N 행렬 세개 A, B, C를 곱하고 더하는, 즉, A x B + C 하는 프로그램
    2. N x N 행렬의 전치 행렬 (전치 행렬이 뭔지는 찾아보세요)을 구하는 프로그램
위 프로그램을 테스트 하기 위해
    3. N x N 행렬의 모든 값을 0보다 크고 (N x N x 10) 보다 작은 임의의(random) 값으로 채워주는 함수
    4. 행렬 N x N을 예쁘게 출력하는 함수
       (예쁘게란 N x N 행렬을 가로 N개, 세로 N 개의 숫자로 줄 맞춰 찍는 것)
3과 4 함수는 1, 2 프로그램에 들어가겠죠?
이렇게 만든 두개(1,2)의 프로그램을 Github에 넣고 각각의 파일 link를 워크시트에 기록합니다. 5월 5일까지."""
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
n = int(input())
originlist = gscal(n)
gsprint(n, originlist)
print()
gsprint(n, gsts(n,originlist))
