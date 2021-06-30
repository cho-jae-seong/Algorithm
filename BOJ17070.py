import sys

def dfs(x,y,shape):
    global ans
    if x==n-1 and y==n-1:
        ans+=1
        return
    if shape==0 or shape==2:
        if y+1<n:
            if board[x][y+1]==0:
                dfs(x,y+1,0)
    if shape==1 or shape==2:
        if x+1<n:
            if board[x+1][y]==0:
                dfs(x+1,y,1)
    if shape==0 or shape==1 or shape==2:
        if x+1<n and y+1<n:
            if board[x+1][y]==0 and board[x][y+1]==0 and board[x+1][y+1]==0:
                dfs(x+1,y+1,2)


ans=0
n=int(sys.stdin.readline())
board=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dfs(0,1,0)
print(ans)