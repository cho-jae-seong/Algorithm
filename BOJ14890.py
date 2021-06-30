import sys

n,l=map(int, sys.stdin.readline().split())
load=[list(map(int, sys.stdin.readline().split()))for i in range(n)]
answer=0

for i in range(n):
    pre=load[i][0]
    cnt=1
    for j in range(1,n):
        if load[i][j]==pre:
            pre=load[i][j]
            cnt+=1
        elif load[i][j]==pre+1 and cnt>=0:
            if cnt>=l:
                cnt=1
                pre=load[i][j]
            else:
                break
        elif load[i][j]==pre-1 and cnt>=0:
            cnt=-l+1
            pre=load[i][j]
        else:
            break
    else:
        if cnt>=0:
            answer+=1

for j in range(n):
    pre=load[0][j]
    cnt=1
    for i in range(1,n):
        if load[i][j]==pre:
            pre=load[i][j]
            cnt+=1
        elif load[i][j]==pre+1 and cnt>=0:
            if cnt>=l:
                cnt=1
                pre=load[i][j]
            else:
                break
        elif load[i][j]==pre-1 and cnt>=0:
            cnt=-l+1
            pre=load[i][j]
        else:
            break
    else:
        if cnt>=0:
            answer+=1
print(answer)
        
        