import sys

n=int(sys.stdin.readline().strip())
paper=[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
white=0
blue=0
def cut(x,y,n):
    global white,blue
    check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:
                cut(x,y,n//2)
                cut(x+n//2,y,n//2)
                cut(x,y+n//2,n//2)
                cut(x+n//2,y+n//2,n//2)
                return
    if check==0:
        white+=1
        return
    else:
        blue+=1
        return
cut(0,0,n)
print(white)
print(blue)