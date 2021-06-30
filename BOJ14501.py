import sys

n=int(sys.stdin.readline())
t,p=[0]*n,[0]*n

for i in range(n):
    t[i],p[i]=map(int, sys.stdin.readline().split())

dp=[0]*25

for i in range(n):
    if dp[i]>dp[i+1]:
        dp[i+1]=dp[i]
    if dp[i+t[i]]<dp[i]+p[i]:
        dp[i+t[i]]=dp[i]+p[i]
print(dp[n])
