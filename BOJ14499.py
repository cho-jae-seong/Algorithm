import sys

n,m,x,y,k=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split()))for i in range(n)]
commands=list(map(int, sys.stdin.readline().split()))
dx,dy=[0,0,-1,1],[1,-1,0,0]
dice,temp=[0]*6,[0]*6
direction=[
    (2,0,5,3,4,1),
    (1,5,0,3,4,2),
    (4,1,2,0,5,3),
    (3,1,2,5,0,4)
]

for c in commands:
    c-=1
    x,y=x+dx[c],y+dy[c]
    if x<0 or x>=n or y<0 or y>=m:
        x-=dx[c];y-=dy[c]
        continue
    for i in range(6):
        temp[i]=dice[i]
    for i in range(6):
        dice[i]=temp[direction[c][i]]
    if board[x][y]:
        dice[5]=board[x][y]
        board[x][y]=0
    else:
        board[x][y]=dice[5]
    print(dice[0])