n=int(input())
A=[]
for i in range(n):
    A.append(list(map(int,input().split())))
B=[]
for i in range(n):
    B.append(int(input()))
A=A[::-1]
B=B[::-1]
for i in range(len(A)):
    if len(set(A[i]))==1:
        A=A[i+1:]
        B=B[i+1:]
        break
A=A[::-1]
B=B[::-1]
ans=0
for i in range(len(A)):
    ans+=B[i]-(i+1)+1
print(ans)
'''
4
0 0 0 0
1 0 0 0
0 1 0 0
0 0 0 0
5
4
1
2'''