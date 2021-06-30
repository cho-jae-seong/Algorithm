import sys

n,k=map(int, sys.stdin.readline().split())
kind=list(map(int, sys.stdin.readline().split()))
plug=[]
cnt=0

for i in range(k):
    if kind[i] in plug:
        continue
    if len(plug)<n:
        plug.append(kind[i])
        continue
    idxs=[]
    for j in range(n):
        try:
            idx=kind[i:].index(plug[j])
        except:
            idx=101
        idxs.append(idx)

    plug_out=idxs.index(max(idxs))
    del plug[plug_out]
    plug.append(kind[i])
    cnt+=1
print(cnt)