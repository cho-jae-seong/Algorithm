import sys
from collections import deque

dx=[1,-1,0,0]
dy=[0,0,-1,1]
def bfs(i,j,char):
    q=deque()
    q.append([i,j])
    chain.append([i,j])
    while q:
        x,y=q.popleft()
        for k in range(4):
            nx=x+dx[k]
            ny=y+dy[k]
            if 0<=nx<12 and 0<=ny<6 and visit[nx][ny]==0 and graph[nx][ny]==char:
                visit[nx][ny]=1
                q.append([nx,ny])
                chain.append([nx,ny])

def down():
    for i in range(6):
        for j in range(10,-1,-1):
            for k in range(11,j,-1):
                if graph[j][i]!='.' and graph[k][i]=='.':
                    graph[k][i]=graph[j][i]
                    graph[j][i]='.'
                    break

graph=[list(sys.stdin.readline().strip()) for _ in range(12)]
answer=0
while True:
    isTrue=False
    visit=[[0]*6 for i in range(12)]
    for i in range(12):
        for j in range(6):
            if graph[i][j]!='.' and visit[i][j]==0:
                visit[i][j]=1
                chain=[]
                bfs(i,j,graph[i][j])
                if len(chain)>3:
                    isTrue=True
                    for x,y in chain:
                        graph[x][y]='.'
    if not isTrue:
        break
    down()
    answer+=1
print(answer)
