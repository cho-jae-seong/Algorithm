import sys
from collections import deque

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(rx,ry,bx,by,cnt):
    q.append([rx,ry,bx,by,cnt])
    check.append([rx,ry,bx,by])
    while len(q)>0:
        rx,ry,bx,by,cnt=q.popleft()
        if board[rx][ry]=='O':
            print(cnt)
            return
        for i in range(4):
            nrx,nry,nbx,nby=rx,ry,bx,by
            while True:
                nrx+=dx[i];nry+=dy[i]
                if board[nrx][nry]=='O':
                    break
                if board[nrx][nry]=='#':
                    nrx-=dx[i];nry-=dy[i]
                    break
            while True:
                nbx+=dx[i];nby+=dy[i]
                if board[nbx][nby]=='O':
                    break
                if board[nbx][nby]=='#':
                    nbx-=dx[i];nby-=dy[i]
                    break
            if board[nbx][nby]=='O':
                continue
            if nrx==nbx and nry==nby:
                if abs(rx-nrx)+abs(ry-nry)>abs(bx-nbx)+abs(by-nby):
                    nrx-=dx[i];nry-=dy[i]
                else:
                    nbx-=dx[i];nby-=dy[i]
            if [nrx,nry,nbx,nby] not in check:
                check.append([nrx,nry,nbx,nby])
                q.append([nrx,nry,nbx,nby,cnt+1])
        if cnt==11:
            print(-1)
            return
    print(-1)
    return

n,m=map(int, sys.stdin.readline().split())
board=[list(map(str, input())) for i in range(n)]
check,q,cnt=[],deque(),0
for i in range(n):
    for j in range(m):
        if board[i][j]=='R':
            rx,ry=i,j
            board[i][j]='.'
        elif board[i][j]=='B':
            bx,by=i,j
            board[i][j]='.'
bfs(rx,ry,bx,by,cnt)