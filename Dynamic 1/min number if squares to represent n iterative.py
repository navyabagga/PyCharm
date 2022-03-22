import math
n=int(input())
dp=[0]*(n+1)
for i in range(1,n+1):
    ans = float("inf")
    for j in range(1,int(math.sqrt(n)+1)):
        cur=1+dp[i-(j*j)]
        ans=min(ans,cur)
    dp[i]=ans
print(dp[n])