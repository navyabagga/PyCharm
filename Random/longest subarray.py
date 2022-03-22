def longestSubarray(arr):
    Max = 1
    s = set()
    for i in range(len(arr) - 1):
        s.add(arr[i])
        for j in range(i + 1, len(arr)):
            if (abs(arr[i] - arr[j]) == 0 or
                    abs(arr[i] - arr[j]) == 1):
                if (not arr[j] in s):
                    if (len(s) == 2):
                        break
                    else:
                        s.add(arr[j])
            else:
                break
        if (len(s) == 2):
            Max = max(Max, j - i)
            s.clear()
        else:
            s.clear()
    return Max

arr=list(map(int,input().split(",")))
l=longestSubarray(arr)
if (l == 1):
    print("-1")
else:
    print(l)