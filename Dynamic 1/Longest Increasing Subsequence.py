def longest(lis,s,e):
    mx=1
    for i in range(s+1,e) :
        if lis[i]>=lis[s]:
            start=longest(lis,s+1,e)
            mx=max(mx,1+start)
    start1=longest(lis,s+1,e)
    maxxx=max(mx,start1)
    return maxxx
n=int(input())
lis=list(map(int,input().split()))
print(longest(lis,0,n))

