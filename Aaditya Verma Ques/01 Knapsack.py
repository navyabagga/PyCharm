def knapsack(n,item,weight,bag,dp):
    if len(item)==0 or bag==0:
        return 0
    if dp[n][bag]!=-1:
        return dp[n][bag]
    if item[n-1]<=bag:
        dp[n][bag]= max(item[n-1]+knapsack(n-1,item,weight,bag-weight[n-1],dp),
                   knapsack(n-1,item,weight,bag,dp))
        return dp[n][bag]
    elif weight[n-1]>bag:
        dp[n][bag]=knapsack(n-1,item,weight,bag,dp)
        return dp[n][bag]
n=int(input())
item=list(map(int,input().split()))
weight=list(map(int,input().split()))
bag=int(input())
dp=[[-1]*(bag+2)]*(n+2)
print("Ans=",knapsack(n,item,weight,bag,dp))