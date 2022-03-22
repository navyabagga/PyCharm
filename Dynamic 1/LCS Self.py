def LIS(lis,dp):
    if len(lis)==0:
        return 0
    dp[0]=1
    for i in range(1,len(lis)):
        for j in range(i):
            if lis[i]>lis[j] and dp[j]>dp[i]:
                dp[i]=dp[j]
        dp[i]+=1

    return max(dp)
lis=list(map(int,input().split()))
n=len(lis)
dp = [0] * n
print(LIS(lis,dp))

