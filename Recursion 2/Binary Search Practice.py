def binary(lis,num,start,end):
    if len(lis)==0:
        return -1
    mid=(start+end)//2
    if lis[mid]==num:
        return mid
    elif lis[mid]>num:
        return binary(lis,num,mid+1,end)
    else:
        return binary(lis,num,start,mid-1)


lis=list(map(int,input().split()))
num=int(input())
start=0
end=len(lis)-1
ans=binary(lis,num,start,end)
if ans==-1:
    print("Element not Found")
else:
    print("Element found at index ",ans+1)