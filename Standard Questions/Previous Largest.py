def printPrevLargest(arr, n):
    ans=[]
    S = list()
    for i in range(n):
        while (len(S) > 0 and S[-1] <= arr[i]):
            S.pop()
        if (len(S) == 0):
            ans.append(-1)
        else:
            ans.append(S[-1])
        S.append(arr[i])
    return ans
arr = list(map(int,input().split()))
n = len(arr)
print(printPrevLargest(arr, n))