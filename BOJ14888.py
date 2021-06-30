import sys

maximum=-987654321
minimum=987654321

def calculate(idx,plus,sub,mul,div,total):
    global maximum
    global minimum
    if idx==n:
        maximum=max(maximum,total)
        minimum=min(minimum,total)
        return
    if plus<p:
        calculate(idx+1,plus+1,sub,mul,div,total+op[idx])
    if sub<s:
        calculate(idx+1,plus,sub+1,mul,div,total-op[idx])
    if mul<m:
        calculate(idx+1,plus,sub,mul+1,div,total*op[idx])
    if div<d:
        if total<0:
            total=-1*total
            calculate(idx+1,plus,sub,mul,div+1,-1*(total//op[idx]))
        else:
            calculate(idx+1,plus,sub,mul,div+1,total//op[idx])

n=int(sys.stdin.readline())
op=list(map(int, sys.stdin.readline().split()))
p,s,m,d=map(int, sys.stdin.readline().split())
calculate(1,0,0,0,0,op[0])
print(maximum)
print(minimum)