def rotate(A):
    transpose = []
    for i in range(len(A)):
        transpose.append([0] * len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            transpose[j][i] = A[i][j]
    return transpose
n=int(input())
matrix=[]
for i in range(n):
    lis=[]
    for j in range(n):
        lis.append(int(input()))
    matrix.append(lis)
mat=rotate(matrix)
for i in mat:
    i.reverse()
for i in mat:
    print(i)

