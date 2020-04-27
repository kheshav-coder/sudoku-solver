from boards import board

def check_empty(board,x,y):
    if board[x][y]==0:
        return True
    else:
        return False

def display(board):
    for i in range(9):
        if i%3==0 and i!=0:
            print("---------------------")
        for j in range(9):
            if j%3==0 and j!=0:
                print("|",end=" ")
            if j==8:
                print(board[i][j])
            else:
                print(board[i][j],end=" ")



def valid(board, num, x,y):
    for i in range(9):
        if board[x][i] == num:
            return False
    for i in range(9):
        if board[i][y] == num:
            return False
    box_y = y // 3
    box_x = x // 3
    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y * 3, box_y*3 + 3):
            if board[i][j] == num:
                return False
    return True


def complete(board):
    v=0
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                v+=1
    if v==0:
        return True
    else:
        return False

def solve(board):
    if complete(board):
        return True
    else:
        for x in range(9):
            for y in range(9):
                if check_empty(board,x,y):
                    for num in range(1,10):
                        if valid(board,num,x,y):
                            board[x][y]=num

                            if solve(board):
                                return True

                            board[x][y]=0
                    return False                  

solve(board)
print(display(board))
