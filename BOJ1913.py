import sys
n=int(sys.stdin.readline().rstrip())
k=int(sys.stdin.readline().rstrip())
snail=[[0]*n for i in range(n)]
value=1
direc=1
count=1
xtemp=int((n-1)//2)
ytemp=int((n-1)//2)
snail[xtemp][ytemp]=value

while value!=n*n:
    if direc==1:
        for i in range(count):
            value+=1
            xtemp-=1
            snail[xtemp][ytemp]=value
            if value==n*n:
                break
        direc=2
    elif direc==2:
        for i in range(count):
            value+=1
            ytemp+=1
            snail[xtemp][ytemp]=value
        count+=1
        direc=3
    elif direc==3:
        for i in range(count):
            value+=1
            xtemp+=1
            snail[xtemp][ytemp]=value
        direc=4
    elif direc==4:
        for i in range(count):
            value+=1
            ytemp-=1
            snail[xtemp][ytemp]=value
        count+=1
        direc=1
for i in range(n):
    for j in range(n):
        print(snail[i][j], end=" ")
        if snail[i][j]==k:
            save_x=i+1
            save_y=j+1
    print()
print(save_x,save_y)