import sys

def tet1(board,x,y):
    if y+3>=m:
        answer1=0
    else:
        answer1=(board[x][y]+board[x][y+1]+board[x][y+2]+board[x][y+3])
    if x+3>=n:
        answer2=0
    else:
        answer2=(board[x][y]+board[x+1][y]+board[x+2][y]+board[x+3][y])
    answer=max(answer1,answer2)
    return answer

def tet2(board,x,y):
    if y+1<m and x+1<n:
        answer=(board[x][y]+board[x][y+1]+board[x+1][y]+board[x+1][y+1])
    else:
        answer=0
    return answer

def tet3(board,x,y):
    if x+2>=n or y+1>=m:
        answer1=0
    else:
        answer1=(board[x][y]+board[x+1][y]+board[x+2][y]+board[x+2][y+1])
    if x+2>=n or y-1<0:
        answer2=0
    else:
        answer2=(board[x][y]+board[x+1][y]+board[x+2][y]+board[x+2][y-1])
    if y+1>=m or x+2>=n:
        answer3=0
    else:
        answer3=(board[x][y]+board[x][y+1]+board[x+1][y+1]+board[x+2][y+1])
    if y+1>=m or x+2>=n:
        answer4=0
    else:
        answer4=(board[x][y]+board[x][y+1]+board[x+1][y]+board[x+2][y])
    if y+2>=m or x+1>=n:
        answer5=0
    else:
        answer5=(board[x][y]+board[x][y+1]+board[x][y+2]+board[x+1][y])
    if x+1>=n or y-2<0:
        answer6=0
    else:
        answer6=(board[x][y]+board[x+1][y]+board[x+1][y-1]+board[x+1][y-2])
    if x+1>=n or y+2>=m:
        answer7=0
    else:
        answer7=(board[x][y]+board[x+1][y]+board[x+1][y+1]+board[x+1][y+2])
    if x+1>=n or y+2>=m:
        answer8=0
    else:
        answer8=(board[x][y]+board[x][y+1]+board[x][y+2]+board[x+1][y+2])
    answer=max(answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8)
    return answer

def tet4(board,x,y):
    if x+2>=n or y+1>=m:
        answer1=0
    else:
        answer1=(board[x][y]+board[x+1][y]+board[x+1][y+1]+board[x+2][y+1])
    if x+2>=n or y-1<0:
        answer2=0
    else:
        answer2=(board[x][y]+board[x+1][y]+board[x+1][y-1]+board[x+2][y-1])
    if x+1>=n or y+1>=m or y-1<0:
        answer3=0
    else:
        answer3=(board[x][y]+board[x][y+1]+board[x+1][y]+board[x+1][y-1])
    if x+1>=n or y+2>=m:
        answer4=0
    else:
        answer4=(board[x][y]+board[x][y+1]+board[x+1][y+1]+board[x+1][y+2])
    answer=max(answer1,answer2,answer3,answer4)
    return answer

def tet5(board,x,y):
    if x+1>=n or y+2>=m:
        answer1=0
    else:
        answer1=(board[x][y]+board[x][y+1]+board[x][y+2]+board[x+1][y+1])
    if x+2>=n or y+1>=m:
        answer2=0
    else:
        answer2=(board[x][y]+board[x+1][y]+board[x+2][y]+board[x+1][y+1])
    if x+2>=n or y-1<0:
        answer3=0
    else:
        answer3=(board[x][y]+board[x+1][y]+board[x+2][y]+board[x+1][y-1])
    if x+1>=n or y-1<0 or y+1>=m:
        answer4=0
    else:
        answer4=(board[x][y]+board[x+1][y]+board[x+1][y-1]+board[x+1][y+1])
    answer=max(answer1,answer2,answer3,answer4)
    return answer

n,m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for i in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        ans1=tet1(board,i,j)
        ans2=tet2(board,i,j)
        ans3=tet3(board,i,j)
        ans4=tet4(board,i,j)
        ans5=tet5(board,i,j)
        ans=max(ans,ans1,ans2,ans3,ans4,ans5)
print(ans)
