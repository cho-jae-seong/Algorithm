import sys

def check(i):
    if i+1<4:
        if turn[i+1]==0 and topni[i][2]!=topni[i+1][6]:
            turn[i+1]=turn[i]*-1
            check(i+1)
    if i-1>=0:
        if turn[i-1]==0 and topni[i][6]!=topni[i-1][2]:
            turn[i-1]=turn[i]*-1
            check(i-1)

topni=[list(map(int, sys.stdin.readline().strip())) for i in range(4)]
k=int(sys.stdin.readline())

for i in range(k):
    idx,direction=map(int, sys.stdin.readline().split())
    turn=[0 for i in range(4)]
    turn[idx-1]=direction
    check(idx-1)
    for i in range(4):
        if turn[i]==0:
            continue
        temp=[0 for i in range(8)]
        if turn[i]==1:
            for j in range(7):
                temp[j+1]=topni[i][j]
            temp[0]=topni[i][7]
        elif turn[i]==-1:
            for j in range(7,0,-1):
                temp[j-1]=topni[i][j]
            temp[7]=topni[i][0]
        topni[i]=temp
ans=0
for i in range(4):
    ans+=topni[i][0]*pow(2,i)
print(ans)
    
