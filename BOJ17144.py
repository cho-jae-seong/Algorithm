import sys

dx=[-1,0,1,0]
dy=[0,1,0,-1]

r,c,t=map(int, sys.stdin.readline().split())
a=[list(map(int, sys.stdin.readline().split())) for i in range(r)]
for _ in range(t):
    temp=[[0]*c for _ in range(r)]
    check=0
    for i in range(r):
        for j in range(c):
            if a[i][j]==-1 and check==0:
                idx1,idy1=i,j
                check+=1
            if a[i][j]==-1 and check==1:
                idx2,idy2=i,j
            if a[i][j]>0:
                cnt=0
                for k in range(4):
                    nr=i+dx[k]
                    nc=j+dy[k]
                    if  0<=nr<r and 0<=nc<c:
                        if a[nr][nc]!=-1:
                            temp[nr][nc]+=a[i][j]//5
                            cnt+=1
                a[i][j]=a[i][j]-(a[i][j]//5)*cnt
    for i in range(r):
        for j in range(c):
            a[i][j]+=temp[i][j]
    temp1=a[idx1][c-1]
    for i in range(c-1,0,-1):
        if a[idx1][i-1]==-1:
            a[idx1][i]=0
        else:
            a[idx1][i]=a[idx1][i-1]
    temp2=a[0][c-1]
    for i in range(0,idx1):
        if i+1==idx1:
            a[i][c-1]=temp1
        else:
            a[i][c-1]=a[i+1][c-1]
    temp3=a[0][0]
    for i in range(0,c-1):
        if i+1==c-1:
            a[0][i]=temp2
        else:
            a[0][i]=a[0][i+1]
    for i in range(idx1-1,0,-1):
        if i-1==0:
            a[i][0]=temp3
        else:
            a[i][0]=a[i-1][0]
    temp4=a[idx2][c-1]
    for i in range(c-1,0,-1):
        if a[idx2][i-1]==-1:
            a[idx2][i]=0
        else:
            a[idx2][i]=a[idx2][i-1]
    temp5=a[r-1][c-1]
    for i in range(r-1,idx2,-1):
        if i-1==idx2:
            a[i][c-1]=temp4
        else: 
            a[i][c-1]=a[i-1][c-1]
    temp6=a[r-1][0]
    for i in range(0,c-1):
        if i+1==c-1:
            a[r-1][i]=temp5
        else:
            a[r-1][i]=a[r-1][i+1]
    for i in range(idx2+1,r-1):
        if i+1==r-1:
            a[i][0]=temp6
        else:
            a[i][0]=a[i+1][0]
sum=0
for i in range(r):
    for j in range(c):
        if a[i][j]!=-1:
            sum+=a[i][j]
print(sum)