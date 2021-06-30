import sys
from collections import deque
from itertools import combinations
from itertools import chain

dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(virus_list):
    dist=[[-1]*n for _ in range(n)]
    dq=deque()
    for pos in virus_list:
        dq.append(pos)
        dist[pos[0]][pos[1]]=0
    max_dist=0
    while dq:
        x,y=dq.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<n and 0<=ny<n and board[nx][ny]!=1 and dist[nx][ny]==-1:
                dist[nx][ny]=dist[x][y]+1
                if board[nx][ny]==0:
                    max_dist=max(max_dist,dist[nx][ny])
                dq.append([nx,ny])
    a=list(chain(*dist))
    if a.count(-1)==list((sum(board,[]))).count(1):
        ans.append(max_dist)


n,m=map(int,sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
starts=deque()
ans=[]
for i in range(n):
    for j in range(n):
        if board[i][j]==2:
            starts.append([i,j])
for now_virus_list in combinations(starts,m):
    bfs(now_virus_list)
print(min(ans) if ans else -1)
