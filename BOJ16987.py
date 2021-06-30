import sys

answer=0

def dfs(eggs,cur):
    global answer
    if cur==len(eggs):
        count=0
        for i in range(len(eggs)):
            if eggs[i][0]<=0:
                count+=1
        if count>answer:
            answer=count
        return
    if eggs[cur][0]<=0:
        dfs(eggs,cur+1)
    else:
        flag=False
        for i in range(len(eggs)):
            if i==cur or eggs[i][0]<=0:
                continue
            eggs[cur][0]-=eggs[i][1]
            eggs[i][0]-=eggs[cur][1]
            flag=True
            dfs(eggs,cur+1)
            eggs[cur][0]+=eggs[i][1]
            eggs[i][0]+=eggs[cur][1]
        if not flag:
            dfs(eggs,cur+1)
    return

n=int(sys.stdin.readline())
eggs=[list(map(int, sys.stdin.readline().split()))for _ in range(n)]
dfs(eggs,0)
print(answer)