import sys

n,m=map(int, sys.stdin.readline().split())
A=[list(sys.stdin.readline().strip())for _ in range(n)]
B=[list(sys.stdin.readline().strip())for _ in range(n)]
answer=0
for i in range(n-2):
    for j in range(m-2):
        if A[i][j]==B[i][j]:
            continue
        answer+=1
        for x in range(i,i+3):
            for y in range(j,j+3):
                if A[x][y]=='0':
                    A[x][y]='1'
                else:
                    A[x][y]='0'
for i in range(n):
    for j in range(m):
        if A[i][j]!=B[i][j]:
            print(-1)
            exit(0)
print(answer)