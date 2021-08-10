import sys

string=sys.stdin.readline().strip()
bomb=sys.stdin.readline().strip()
lastbomb=bomb[-1]
lenbomb=len(bomb)
stack=[]
for char in string:
    stack.append(char)
    if char==lastbomb and ''.join(stack[-lenbomb:])==bomb:
        del stack[-lenbomb:]
answer=''.join(stack)
if answer=='':
    print('FRULA')
else:
    print(answer)