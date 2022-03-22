def exp(s,l,h,palin):
    while l >= 0 and h < len(s) and s[l] == s[h]:
        palin.append(s[l: + 1])
        l=l-1
        h=h+1


def palinSub(s):
    palin=[]
    for i in range(len(s)):
        exp(s,i,i,palin)
        exp(s,i,i+1,palin)
    return palin


length=int(input())
s=input()
n=int(input())
lis2=[]
c=0
lis2=list(map(int,input().split()))[:n]
lis1=list(palinSub(s))
if 1 in lis2:
    c=c+len(s)
for i in range(len(lis1)):
    for j in lis2:
        if(len(lis1[i])==j and j!=1):
            c+=1
print(c,end="")