import sys
import copy

def find_max(array):
    global answer
    for i in range(n):
        for j in range(n):
            if answer<array[i][j]:
                answer=array[i][j]

def move_left(board):
    for i in range(n):
        x=0
        p=0
        for j in range(n):
            if board[i][j]==0:
                continue
            if x==0:
                x=board[i][j]
            else:
                if x==board[i][j]:
                    board[i][p]=2*x
                    p+=1
                    x=0
                else:
                    board[i][p]=x
                    p+=1
                    x=board[i][j]
            board[i][j]=0
        if x!=0:
            board[i][p]=x
    return board

def move_right(board):
    for i in range(n):
        x=0
        p=n-1
        for j in range(n-1,-1,-1):
            if board[i][j]==0:
                continue
            if x==0:
                x=board[i][j]
            else:
                if x==board[i][j]:
                    board[i][p]=2*x
                    p-=1
                    x=0
                else:
                    board[i][p]=x
                    p-=1
                    x=board[i][j]
            board[i][j]=0
        if x!=0:
            board[i][p]=x
    return board

def move_up(board):
    for i in range(n):
        x=0
        p=0
        for j in range(n):
            if board[j][i]==0:
                continue
            if x==0:
                x=board[j][i]
            else:
                if x==board[j][i]:
                    board[p][i]=2*x
                    p+=1
                    x=0
                else:
                    board[p][i]=x
                    p+=1
                    x=board[j][i]
            board[j][i]=0
        if x!=0:
            board[p][i]=x
    return board

def move_down(board):
    for i in range(n):
        x=0
        p=n-1
        for j in range(n-1,-1,-1):
            if board[j][i]==0:
                continue
            if x==0:
                x=board[j][i]
            else:
                if x==board[j][i]:
                    board[p][i]=2*x
                    p-=1
                    x=0
                else:
                    board[p][i]=x
                    p-=1
                    x=board[j][i]
            board[j][i]=0
        if x!=0:
            board[p][i]=x
    return board

def dfs(dfs_block,cnt):
    if cnt==5:
        find_max(dfs_block)
        return
    dfs(move_left(copy.deepcopy(dfs_block)),cnt+1)
    dfs(move_right(copy.deepcopy(dfs_block)),cnt+1)
    dfs(move_up(copy.deepcopy(dfs_block)),cnt+1)
    dfs(move_down(copy.deepcopy(dfs_block)),cnt+1)

n=int(sys.stdin.readline())
block=[]
answer=0
for i in range(n):
    block.append(list(map(int, sys.stdin.readline().split())))
dfs(block,0)
print(answer)
    