import sys

m,n=map(int, sys.stdin.readline().split())
board=[[0]*n for i in range(m)]
check=1
direc=1
answer=0
xtemp=0
ytemp=0

board[xtemp][ytemp]=1

while check!=m*n:
    if direc==1:
        ytemp+=1
        if ytemp<n and board[xtemp][ytemp]==0:
            board[xtemp][ytemp]=1
            check+=1
        else:
            answer+=1
            ytemp-=1
            direc=2
    elif direc==2:
        xtemp+=1
        if xtemp<m and board[xtemp][ytemp]==0:
            board[xtemp][ytemp]=1
            check+=1
        else:
            answer+=1
            xtemp-=1
            direc=3
    elif direc==3:
        ytemp-=1
        if 0<=ytemp and board[xtemp][ytemp]==0:
            board[xtemp][ytemp]=1
            check+=1
        else:
            answer+=1
            ytemp+=1
            direc=4
    elif direc==4:
        xtemp-=1
        if 0<=xtemp and board[xtemp][ytemp]==0:
            board[xtemp][ytemp]=1
            check+=1
        else:
            answer+=1
            xtemp+=1
            direc=1
print(answer)
