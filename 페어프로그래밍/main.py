
    # 스도쿠 해독기 만들기
    # 조건은 9 x 9 사이즈, 그리고 3 x 3 사이즈에서 1부터 9까지 하나씩
tfa = [0,1,2],[3,4,5], [6,7,8] # 9 * 9 범위 찾으려고..
puzzle = []
for i in range(9):
    puzzle.append(list(map(int,input().split())))



"""puzzle = [
        [4,2,9,0,0,1,0,5,8],
        [0,0,8,4,0,9,0,0,2],
        [0,7,0,8,0,3,0,9,0],
        [0,8,0,9,0,0,0,0,3],
        [0,0,3,0,0,0,5,0,0],
        [5,0,0,0,0,2,0,8,0],
        [0,5,0,2,0,7,0,3,0],
        [3,0,0,5,0,4,8,0,0],
        [9,6,0,1,0,0,4,7,5]
    ]"""
def board_33(board, row, col): # 33 범위 만드는 함수
    board33 = []
    g, s = 0, 0
    for i, sublist in enumerate(tfa):
        if row in sublist:
            g = i
            break
    for i, sublist in enumerate(tfa):
        if col in sublist:
            s = i
            break
    for i in tfa[g]:
        for j in tfa[s]:
            board33.append(board[i][j])
    return board33

def is_valid(board,row,col,num): ## 유효성 검사!!!
    if num < 1 or num > 9: ## 입력값이 문제 없긴 해도 혹시모르니까 한번 체크하고 가기
        return False
    board33 = board_33(board, row, col) ## 9칸을 불러오는 함수
    garo = board[row] # 가로칸
    sero = [] # 세로칸 선언
    for i in range(0, 9):
        sero.append(board[i][col])
    if num not in garo:
        if num not in sero:
            if num not in board33: #수가 가로열, 세로열, 9칸에 없어야만 True를 반환함
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def solve_sudoku(board):
    for i in range(0, 9):
        for j in range(0, 9):
            if board[i][j] == 0: # 좌표의 칸이 공칸인지 확인합니다
                for num in range(1, 10): # 상수의 범위 입니다!
                    if is_valid(board, i, j, num): # is_valid가 Return 한 값이 True이면 (즉 i j에 num을 넣을 수 있으면)
                        board[i][j] = num # 스도쿠의 i j에 num 값을 넣어줍니다
                        if solve_sudoku(board): # 그리고 그 다음의 값을 확인하면서 재귀함수가 되는데... 위 과정을 무한반복하지요.
                            return True
                    board[i][j] = 0 # 그렇게 재귀함수로 진행하다가, 만약 is_valid에서 False로 반환되면? 이전값이 틀렸네? 어쩔 수 없어 그럼 0으로 바꿔
                return False # 상수의 범위에서 오류가 생기거나, 내부 로직에서 board[i][j]를 0으로 바꿨을 때 출력함!
    return True #모든게 끝나서 True로 리턴합니다!

def print_board(board):
    print("\n-----Sudoku Answer-----")
    for i in range (9):
        print(*board[i])
# 재귀함수야 세상에서 사라지거라!

if solve_sudoku(puzzle):
    print_board(puzzle)
else:
    print("풀 수 없는 스도쿠입니다.")
    #재귀와 백트래킹을 사용하여 스도쿠를 해결합니다
    #9 * 9 배열에 빈칸을 찾아 가능한 숫자를 넣고 재귀적으로 다음칸에 넣습니다
    # 넣을수가 없으면 이전 스텝에 문제가 있었으므로 backtraking
    # 모든칸이 채워지면 성공
    # 가능한 num이 발견되면 board[row][col] = num
    # is_valid(board, row+1, col+1, 1)