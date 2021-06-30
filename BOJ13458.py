import sys

n=int(sys.stdin.readline())
people=list(map(int, sys.stdin.readline().split()))
b,c=map(int,sys.stdin.readline().split())
answer=0
for i in range(n):
    people[i]-=b
    answer+=1
    if people[i]>0:
        if people[i]%c==0:
            answer+=(people[i]//c)
        else:
            answer+=(people[i]//c+1)
print(answer)