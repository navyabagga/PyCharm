def knapsack(weight, cost, maxweight, n):
    if maxweight==0 or n==0:
        return 0
    if dp[maxweight][n]!=-1:
        return dp[maxweight][n]
    if weight[n-1]<=maxweight:
        dp[maxweight][n]=max(cost[n-1]+knapsack(weight, cost, maxweight-weight[n-1],n-1),
                   knapsack(weight, cost, maxweight,n-1))
        return dp[maxweight][n]
    elif weight[n-1]>maxweight:
        dp[maxweight][n]=knapsack(weight,cost,maxweight,n-1)
        return dp[maxweight][n]
weight=list(map(int,input().split()))
cost=list(map(int,input().split()))
maxweight=int(input())
n=len(weight)
dp=[[-1]*(n+1)]*(maxweight+1)
print(knapsack(weight,cost,maxweight,n))
for i in dp:
    print(i)