def binary(lis,start,end,num):
    if start>end:
        return -1
    mid=(start+end)//2
    if lis[mid]==num:
        return mid
    elif lis[mid]>num:
        return binary(lis,start,mid-1,num)
    else:
        return binary(lis, mid+1, end, num)

lis=list(map(int,input().split()))
start=0
end=len(lis)-1
num=int(input())
ans=binary(lis,start,end,num)
if ans == -1:
    print("Element not found")
else:
    print("Element found at ",ans+1)
