def subset(lis,s):
    if len(lis)==0 or s==0:
        return False
    if len(lis)==1:
        if lis[0]==s:
            return True
        return False
    n=len(lis)
    if lis[n - 1] <= s:
        return max(lis[n - 1] + subset(lis,s-lis[n-1]),subset(lis,))
    elif lis[n - 1] > s:
        return subset(lis,s)