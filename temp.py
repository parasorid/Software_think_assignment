tfa = [0,1,2],[3,4,5], [6,7,8]
puzzle = []
for i in range(9):
    puzzle.append(list(map(int,input().split())))
def board_33(board, row, col):
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

def is_valid(board,row,col,num):
    if num < 1 or num > 9:
        return False
    board33 = board_33(board, row, col)
    garo = board[row]
    sero = []
    for i in range(0, 9):
        sero.append(board[i][col])
    if num not in garo:
        if num not in sero:
            if num not in board33:
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
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                    board[i][j] = 0
                return False
    return True

def print_board(board):
    print("\n-----Sudoku Answer-----")
    for i in range (9):
        print(*board[i])

if solve_sudoku(puzzle):
    print_board(puzzle)
else:
    print("풀 수 없는 스도쿠입니다.")