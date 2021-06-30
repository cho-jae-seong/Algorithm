dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(r,c,d):
    global ans
    if arr[r][c]==0:
        arr[r][c]=2
        ans+=1
    for i in range(4):
        nd=(d+3)%4
        nr=r+dx[nd]
        nc=c+dy[nd]
        if arr[nr][nc]==0:
            dfs(nr,nc,nd)
            return
        d=nd
    nd=(d+2)%4
    nr=r+dx[nd]
    nc=c+dy[nd]
    if arr[nr][nc]==1:
        return
    dfs(nr,nc,d)
    

n,m=map(int, input().split())
r,c,d=map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(n)]
ans=0
dfs(r,c,d)
print(ans)