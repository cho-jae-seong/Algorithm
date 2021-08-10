import sys

def dfs(idx,cnt):
    global answer
    if cnt==k-5:
        read_cnt=0
        for word in words:
            for w in word:
                if not learn[ord(w)-ord('a')]:
                    break
            else:
                read_cnt+=1
        answer=max(answer,read_cnt) if answer else read_cnt
        return
    for i in range(idx,26):
        if not learn[i]:
            learn[i]=True
            dfs(i,cnt+1)
            learn[i]=False


answer=None
n,k=map(int, sys.stdin.readline().split())
if k<5:
    print(0)
    exit(0)
if k==26:
    print(n)
    exit(0)
words=[set(sys.stdin.readline().rstrip()) for _ in range(n)]
learn=[False]*26
for c in ('a','c','i','n','t'):
    learn[ord(c)-ord('a')]=True
dfs(0,0)
print(answer)