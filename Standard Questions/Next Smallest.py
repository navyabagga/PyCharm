def printNSE(arr):
    s = []
    mp = []
    for i in range(len(arr)):
        print(i)
        while arr[i]>= s[-1] and len(s)!=0:
            s.pop()
        if len(s)==0:
            mp.append(-1)
            s.append(arr[i])
        mp.append(s[-1])
    print(mp)
arr=list(map(int,input().split()))
print(printNSE(arr))