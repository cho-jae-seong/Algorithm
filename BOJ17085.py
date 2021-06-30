import sys

def dfs(x,y):
    size=0
    while -1<x-size and x+size<n and -1<y-size and y+size<m and board[x-size][y]==board[x+size][y]==board[x][y-size]==board[x][y+size]=='#':
        size+=1
    while size:
        dotinfo.append([size,x,y])
        size-=1

def test(dot1,dot2):
    testBoard=[[0]*m for _ in range(n)]
    d=[[-1,0],[1,0],[0,-1],[0,1]]

    for i in range(dot1[0]):
        for j in range(4):
            testBoard[dot1[1]+d[j][0]*i][dot1[2]+d[j][1]*i]=1
    for i in range(dot2[0]):
        for j in range(4):
            if testBoard[dot2[1]+d[j][0]*i][dot2[2]+d[j][1]*i] == 1:
                return False
    return True
    

n,m=map(int, sys.stdin.readline().split())
board=[list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dotinfo=[]
result=0

for i in range(n):
    for j in range(m):
        if board[i][j]=='#':
            dfs(i,j)

for i in range(len(dotinfo)-1):
    for j in range(i+1,len(dotinfo)):
        mul = (1+(dotinfo[i][0]-1)*4)*(1+(dotinfo[j][0]-1)*4)
        if mul>result and test(dotinfo[i],dotinfo[j]):
            result=mul
print(result)