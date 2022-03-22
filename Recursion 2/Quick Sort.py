def partition(lis,start,end):
    p=lis[start]
    c=0
    for i in range(start,end+1):
        if lis[i]<p:
            c+=1
    lis[start+c],lis[start]=lis[start],lis[start+c]
    piv=start+c
    i=start
    j=end
    if i<j:
        if lis[i]<p:
            i=i+1
        elif lis[j]>=p:
            j=j-1
        else:
            lis[i],lis[j]=lis[j],lis[i]
            i=i+1
            j=j-1
    return piv
def quick_sort(lis,start,end):
    if start>=end:
        return
    piv_in=partition(lis,start,end)
    quick_sort(lis,start,piv_in-1)
    quick_sort(lis,piv_in+1,end)

lis=list(map(int,input().split()))
start=0
end=len(lis)
print(quick_sort(lis,start,end))

