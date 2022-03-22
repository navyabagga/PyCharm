def minSteps(n):
    if n==1:
        return 0
    ans=float("inf")
    ans1=minSteps(n-1)
    ans2=float("inf")
    ans3=float("inf")
    if n%2==0:
        ans2=minSteps(n/2)
    if n%3==0:
        ans3=minSteps(n/3)
    ans=1+min(ans1,ans2,ans3)
    return ans
n=int(input())
print(minSteps(n))