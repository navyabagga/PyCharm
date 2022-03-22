import math
def minSq(n):
    if n==0:
        return 0
    ans=float("inf")
    s=int(math.sqrt(n))
    for i in range(1,s+1):
        if dp[n-(i*i)]!=0:
            ab=dp[n-(i*i)]
        else:
            ab=minSq(n-(i*i))
            dp[n-(i*i)]=ab
        ans=min(ans,1+ab)
    return ans
n=int(input())
dp=[0]*(n+1)
print(minSq(n))
print(dp)