arr=list(map(int,input().split()))
def wine(arr,y,start,end,dp):
    if start>end:
        return 0
    if dp[start][end]!=0:
        return dp[start][end]
    a=(arr[start]*y)+wine(arr,y+1,start+1,end,dp)
    b=(arr[end]*y)+wine(arr,y+1,start,end-1,dp)
    dp[start][end]=max(a,b)
    return dp[start][end]
dp=[[0]*len(arr) for i in range(len(arr))]
ans=wine(arr,1,0,len(arr)-1,dp)

print(ans)
