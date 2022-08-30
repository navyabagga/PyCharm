n,x=map(int,input().split())
L=list(map(int,input().split()))
lis=[L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)]
count=0
for i in lis:
    y=0
    for j in range(len(i)):
        y^=i[j]
    if y<x:
        count+=1
print(count)