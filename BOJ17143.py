import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dir(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    else: return 3

R,C,M=map(int, sys.stdin.readline().split())
board=[[0]*C for _ in range(R)]
q=[]
for _ in range(M):
    x,y,s,d,z=map(int, sys.stdin.readline().split())
    board[x-1][y-1]=[s,d,z]
    q.append([x-1,y-1])
ans,rx,ry=0,-1,-1
for col in range(C):
    for i in range(R):
        if board[i][col]:
            ans+=board[i][col][2]
            board[i][col]=0
            rx,ry=i,col
            break
    qlen=len(q)
    temp=[[0]*C for _ in range(R)]
    q2=[]
    for i in range(qlen):
        x,y=q[i]
        if x==rx and y==ry:
            continue
        s,d,z=board[x][y][0],board[x][y][1],board[x][y][2]

        if d==1 or d==2:
            nx,ny=x+s*dx[d-1],y
            if not 0<=nx<R:
                temp_s=s
                if d==1:
                    s-=x
                    x=0
                else:
                    s-=R-1-x
                    x=R-1
                d=dir(d)
                f,g=s//(R-1),s%(R-1)
                if f%2==0:
                    if x==0:
                        nx=g
                    else:
                        nx=R-1-g
                else:
                    if x==0:
                        nx=R-1-g
                    else:
                        nx=g
                    d=dir(d)
                s=temp_s
        else:
            nx,ny=x,y+s*dy[d-1]
            if not 0<=ny<C:
                temp_s=s
                if d==3:
                    s-=C-1-y
                    y=C-1
                else:
                    s-=y
                    y=0
                d=dir(d)
                f,g=s//(C-1),s%(C-1)
                if f%2==0:
                    if y==0:
                        ny=g
                    else:
                        ny=C-1-g
                else:
                    if y==0:
                        ny=C-1-g
                    else:
                        ny=g
                    d=dir(d)
                s=temp_s
        if temp[nx][ny]:
            if z>temp[nx][ny][2]:
                temp[nx][ny]=[s,d,z]
        else:
            temp[nx][ny]=[s,d,z]
            q2.append([nx,ny])
    board=temp
    q=q2
print(ans)

                

