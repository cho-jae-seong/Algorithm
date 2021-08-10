import sys

n=int(sys.stdin.readline().strip())
word=list(sys.stdin.readline().strip() for _ in range(n))
word.sort(key=len)
answer=0
for i in range(n):
    temp=word[i]
    isHead=False
    for j in range(i+1,n):
        try:
            if word[j].index(temp)==0:
                isHead=True
                break
        except:
            continue
    if not isHead:
        answer+=1
print(answer)