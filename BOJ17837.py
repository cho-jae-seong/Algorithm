import sys

dx=[0,0,-1,1]
dy=[1,-1,0,0]

def move(chess_num):
    x,y,z=chess[chess_num]
    nx=x+dx[z]
    ny=y+dy[z]
    if not 0<=nx<n or not 0<=ny<n or board[nx][ny]==2:
        if z==0:
            nz=1
        elif z==1:
            nz=0
        elif z==2:
            nz=3
        else:
            nz=2
        chess[chess_num][2]=nz
        nx=x+dx[nz]
        ny=y+dy[nz]
        if not 0<=nx<n or not 0<=ny<n or board[nx][ny]==2:
            return 0
    temp=[]
    for i,key in enumerate(chess_map[x][y]):
        if key==chess_num:
            temp.extend(chess_map[x][y][i:])
            chess_map[x][y]=chess_map[x][y][:i]
            break
    if board[nx][ny]==1:
        temp=temp[-1::-1]
    for i in temp:
        chess_map[nx][ny].append(i)
        chess[i][:2]=[nx,ny]
    if len(chess_map[nx][ny])>=4:
        return 1
    return 0

n,k=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chess_map=[[[]for _ in range(n)] for _ in range(n)]
chess=[0 for _ in range(k)]
for _ in range(k):
    x,y,d=map(int, sys.stdin.readline().split())
    chess_map[x-1][y-1].append(_)
    chess[_]=[x-1,y-1,d-1]

cnt=1
while cnt<=1000:
    for i in range(k):
        flag=move(i)
        if flag:
            print(cnt)
            exit(0)
    cnt+=1
print(-1)