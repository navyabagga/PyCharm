def knapsack(weight, cost, maxweight, n):
    if maxweight==0 or n==0:
        return 0
    if weight[n-1]<=maxweight:
        return max(cost[n-1]+knapsack(weight, cost, maxweight-weight[n-1],n-1),
                   knapsack(weight, cost, maxweight,n-1))
    elif weight[n-1]>maxweight:
        return knapsack(weight,cost,maxweight,n-1)
weight=list(map(int,input().split()))
cost=list(map(int,input().split()))
maxweight=int(input())
n=len(weight)
print(knapsack(weight,cost,maxweight,n))