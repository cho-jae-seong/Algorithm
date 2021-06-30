import sys

def move():
    for i in range(n):
        num=i
        for j in range(h):
            if sadari[num][j]:
                num+=1
            elif sadari[num-1][j]:
                num-=1
        if i!=num:
            return 0
    return 1

def dfs(cnt,idx,r):
    global ans
    if cnt==r:
        if move():
            ans=cnt
        return

    for i in range(idx,h):
        for j in range(n-1):
            if sadari[j][i]:
                continue
            if j-1>=0 and sadari[j-1][i]:
                continue
            if j+1<n and sadari[j+1][i]:
                continue
            sadari[j][i]=1
            dfs(cnt+1,i,r)
            sadari[j][i]=0
        

n,m,h=map(int, sys.stdin.readline().split())
sadari=[[0]*h for i in range(n)]
for i in range(m):
    a,b=map(int, sys.stdin.readline().split())
    sadari[b-1][a-1]=1
ans=sys.maxsize
flag=1
for r in range(4):
    dfs(0,0,r)
    if ans!=sys.maxsize:
        print(ans)
        flag=0
        break
if flag:
    print(-1)
