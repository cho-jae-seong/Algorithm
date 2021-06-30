import sys

n,m=map(int, sys.stdin.readline().split())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
h,w,sr,sc,fr,fc=map(int, sys.stdin.readline().split())
sr,sc,fr,fc=sr-1,sc-1,fr-1,fc-1
visited=[[0 for i in range(m)] for j in range(n)]
walls=[]
for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            walls.append((i,j,))

def check(nx,ny):
    if nx+h-1>=n or ny+w-1>=m:
        return False
    
    for i,j in walls:
        if nx<=i<nx+h and ny<=j<ny+w:
            return False
    return True

queue=[]
queue.append((0,sr,sc))
while queue:
    path,x,y=queue.pop(0)
    if x==fr and y==fc:
        print(path)
        exit()
    for dx,dy in [[-1,0],[1,0],[0,-1],[0,1]]:
        nx=x+dx
        ny=y+dy
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if not check(nx,ny):
            continue
        if not visited[nx][ny]:
            visited[nx][ny]=1
            queue.append((path+1,nx,ny))
print(-1)