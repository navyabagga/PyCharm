t = int(input())
result=[]
for x in range(t):
    n = int(input())
    n = str(n)
    sum = 0
    lis=float("inf")
    for i in n:
        sum = sum + int(i)
    sum = 9 - (sum % 9)
    if sum!=9:
        lis=min(lis,int((str(sum) + n)))
        lis=min(lis,int(n + str(sum)))
        for i in range(1, len(n)):
            lis=min(lis,int(n[:i] + str(sum) + n[i:]))
        result.append(lis)
    else:
        result.append(n[:1] + str(0) + n[1:])
for i in range(len(result)):
    print("Case #" + str(i + 1) + ":", result[i])
