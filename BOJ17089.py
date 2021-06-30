import sys

n,m=map(int, sys.stdin.readline().split())
relation=[[False]*(n+1)for _ in range(n+1)]
friends=[0]*(n+1)
answer=sys.maxsize

for i in range(m):
    me,my_friend=map(int, sys.stdin.readline().split())
    relation[me][my_friend]=True
    relation[my_friend][me]=True
    friends[me]+=1
    friends[my_friend]+=1

for i in range(n+1):
    for j in range(i+1,n+1):
        if relation[i][j]:
            for k in range(j+1,n+1):
                if relation[i][k] and relation[j][k]:
                    answer=min(answer, friends[i]+friends[j]+friends[k]-6)
print(-1 if answer==sys.maxsize else answer)