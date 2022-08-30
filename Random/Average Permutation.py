from itertools import permutations
n=int(input())
lis=[i+1 for i in range(n)]
perm=permutations(lis)
mn=[]
for i in perm:
    ans=[]
    for j in range(len(i)-2):
        ans.append((i[j]+i[j+1]+i[j+2])/3)
    print(i,sum(ans))
    mn.append(sum(ans))
print(min(mn))
