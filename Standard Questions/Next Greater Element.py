def NextGreaterElement():
    s = []
    res = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        if (len(s) != 0):
            while (len(s) != 0 and s[-1] <= arr[i]):
                s.pop()
        res[i] = -1 if len(s) == 0 else s[-1]
        s.append(arr[i])
    print(s)