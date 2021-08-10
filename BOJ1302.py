import sys

n=int(sys.stdin.readline().strip())
book={}
for i in range(n):
    title=sys.stdin.readline().strip()
    if title in book:
        book[title]+=1
    else:
        book[title]=1
book=sorted(book.items(), key=lambda x:(-x[1],x[0]))
print(book[0][0])