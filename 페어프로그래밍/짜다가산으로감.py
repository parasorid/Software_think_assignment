# 스도쿠 해독기 만들기
# 조건은 9 x 9 사이즈, 그리고 3 x 3 사이즈에서 1부터 9까지 하나씩
puzzle = [
        [4,2,9,0,0,1,0,5,8],
        [0,0,8,4,0,9,0,0,2],
        [0,7,0,8,0,3,0,9,0],
        [0,8,0,9,0,0,0,0,3],
        [0,0,3,0,0,0,5,0,0],
        [5,0,0,0,0,2,0,8,0],
        [0,5,0,2,0,7,0,3,0],
        [3,0,0,5,0,4,8,0,0],
        [9,6,0,1,0,0,4,7,5]
    ]

# 좌표의 위치에 들어갈 수 있는지 판독하는 함수
def is_valid(board, row, col, num):
    if (row >9 or col >9):
        exit()
    garo = puzzle[row]
    sero = []
    board3 = []
    for i in range(9):
        sero.append(puzzle[i][col])
    if row in set([0, 1, 2]):
        if col in set([0, 1, 2]):
            for i in range(0, 3):
                for j in range(0, 3):
                    board3.append(board[i][j])
    for k in range(0, 9):
        if k not in garo:
            if k not in sero:
                if k not in board3:
                    board[row][col] = k
                    is_valid(board, row, col, board[row][col])
                else:
                    pass
            else:
                pass
        else: pass
is_valid(puzzle, 1, 2, puzzle[1][2])
for i in range(9):
    print(puzzle[i])

# 재귀와 백 트래킹을 이용해서 스도쿠를 해결하는 함수
def solve_sudoku(board):
    print(1)

#그냥 단순히 해답을 출력하는 함수
def print_board(board):
    print(1)


#그냥 풀이 가능한지 확인하기
"""if solve_sudoku(puzzle):
    print_board(puzzle)
else:
    print("해답따위 없다.")

for i in range(9):
    for j in range(9):
        num = puzzle[i][j]
        if num == 0:
            is_valid(what, i, j, num)"""