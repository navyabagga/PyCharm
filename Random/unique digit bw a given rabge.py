import math
n=int(input())
a=math.pow(10,n)
ans=[]
for i in range(0,int(a)):
    s=list(str(i))
    ss=list(set(s))
    if len(ss)==len(s):
        print(i)
        ans.append(i)
print(len(ans))