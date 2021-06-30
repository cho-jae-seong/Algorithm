import sys

n,m,k=map(int, sys.stdin.readline().split())
a=[list(map(int, sys.stdin.readline().split())) for i in range(n)]
tree=[[[]for i in range(n)]for j in range(n)]
for i in range(m):
    x,y,z=map(int, sys.stdin.readline().split())
    tree[x-1][y-1].append(z)
ground=[[5]*n for i in range(n)]

for _ in range(k):
    for i in range(n):
        for j in range(n):
            if len(tree[i][j])<=0:
                continue
            tree[i][j].sort()
            idx=0
            while idx<len(tree[i][j]):
                if tree[i][j][idx]<=ground[i][j]:
                    ground[i][j]-=tree[i][j][idx]
                    tree[i][j][idx]+=1
                    idx+=1
                else:
                    die=tree[i][j][idx:]
                    for now in die:
                        ground[i][j]+=(now//2)
                    tree[i][j]=tree[i][j][:idx]
                    break
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    for i in range(n):
        for j in range(n):
            c=0
            if tree[i][j]:
                for now in tree[i][j]:
                    if now%5==0:
                        c+=1
            if c>0:
                for k in range(8):
                    ni=i+dx[k]
                    nj=j+dy[k]
                    if 0<=ni<n and 0<=nj<n:
                        for q in range(c):
                            tree[ni][nj].append(1)
    for i in range(n):
        for j in range(n):
            ground[i][j]+=a[i][j]
ans=0
for i in range(n):
    for j in range(n):
        ans+=len(tree[i][j])
print(ans)