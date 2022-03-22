def isSubsequence(s,t):
    if len(t) < len(s):
        return False
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i == len(s):
        return True
    else:
        return False

t=int(input())
result=[]
for _ in range(t):
    i=str(input())
    p=str(input())
    tf=isSubsequence(i,p)
    if tf==True:
        ans=len(p)-len(i)
        result.append(ans)
    else:
        result.append("IMPOSSIBLE")
for i in range(len(result)):
    print("Case #"+str(i+1)+":",result[i])