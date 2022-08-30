n=int(input())
lis=[]
visit=[]
for i in range(n):
    a=list(map(str, input().split()))
    lis.append(a)
    b=[0]*n
    visit.append(b)
visit[0][0]=1
i=0
j=0
while i<n:
    while j<n:
        if i==0 and j==0:
            pos1=lis[0][j+1]
            pos2=lis[i+1][0]
            pos3=lis[i+1][j+1]
            if pos1=="R" and visit[0][j+1]!=1:
                j=j+1
                visit[0][j+1]=1
            elif pos2=="R" and visit[i+1][0]!=1:
                i+=1
                visit[i+1][0] = 1
            elif pos3=="R" and visit[i+1][j+1]!=1:
                i+=1
                j+=1
                visit[i+1][j + 1] = 1
        elif i==(n-1) and j==(n-1):
            pos1=lis[n-2][n-1]
            pos2=lis[n-1][n-2]
            pos3=lis[n-2][n-2]
            if pos1=="R" and visit[n-2][n-1]!=1:
                i=n-2
                visit[n-2][n-1]=1
            elif pos2=="R" and visit[n-1][n-2]!=1:
                j=n-2
                visit[n-1][n-2]= 1
            elif pos3=="R" and visit[n-2][n-2]!=1:
                i=n-2
                j=n-2
                visit[n-2][n-2] = 1
        elif i==(n-1) and j==0:
            pos1=lis[n-2][0]
            pos2=lis[n-1][1]
            pos3=lis[n-2][1]
            if pos1=="R" and visit[n-2][j]!=1:
                i=n-2
                visit[n-2][0]=1
            elif pos2=="R" and visit[n-1][j]!=1:
                j+=1
                visit[n-1][1]= 1
            elif pos3=="R" and visit[n-2][j]!=1:
                i=n-2
                j+=1
                visit[n-2][1] = 1
        elif i==0 and j==n-1:
            pos1=lis[0][n-2]
            pos2=lis[i+1][n-2]
            pos3=lis[i+1][n-1]
            if pos1=="R" and visit[i][j-1]!=1:
                j-=1
                visit[i][n-2]=1
            elif pos2=="R" and visit[i+1][j-1]!=1:
                i+=1
                j-=1
                visit[i+1][n-2]= 1
            elif pos3=="R" and visit[i+1][j]!=1:
                i+=1
                visit[i+1][n-1] = 1
        elif i==0:
            pos1=lis[i][j-1]
            pos2=lis[i+1][j-1]
            pos3=lis[i+1][j]
            pos4=lis[i+1][j+1]
            pos5=lis[i][j+1]
            if pos1=="R" and visit[i][j+1]!=1:
                j+=1
                visit[i][j+1]=1
            elif pos2=="R" and visit[i+1][j-1]!=1:
                i+=1
                j-=1
                visit[i+1][j-1]=1
            elif pos3=="R" and visit[i+1][j]!=1:
                i+=1
                visit[i+1][j]=1
            elif pos4=="R" and visit[i+1][j+1]!=1:
                i+=1
                j+=1
                visit[i+1][j+1]=1
            elif pos5=="R" and visit[i][j+1]!=1:
                j+=1
                visit[i][j+1]=1
        elif i==(n-1):
            pos1=lis[i][j-1]
            pos2=lis[i-1][j-1]
            pos3=lis[i-1][j]
            pos4=lis[i-1][j+1]
            pos5=lis[i][j+1]
            if pos1=="R" and visit[i][j-1]!=1:
                j-=1
                visit[i][j+1]=1
            elif pos2=="R" and visit[i-1][j-1]!=1:
                i-=1
                visit[i-1][j-1]=1
            elif pos3=="R" and visit[i-1][j]!=1:
                i-=1
                visit[i-1][j]=1
            elif pos4=="R" and visit[i-1][j+1]!=1:
                i-=1
                j+=1
                visit[i+1][j+1]=1
            elif pos5=="R" and visit[i][j+1]!=1:
                j+=1
                visit[i][j+1]=1
        elif j==0:
            pos1 = lis[i-1][j]
            pos2 = lis[i-1][j+1]
            pos3 = lis[i][j+1]
            pos4 = lis[i + 1][j + 1]
            pos5 = lis[i+1][j]
            if pos1 == "R" and visit[i-1][j] != 1:
                i-=1
                visit[i-1][j] = 1
            elif pos2 == "R" and [i-1][j+1] != 1:
                i -= 1
                j += 1
                visit[i-1][j+1] = 1
            elif pos3 == "R" and visit[i][j+1] != 1:
                j += 1
                visit[i][j+1]= 1
            elif pos4 == "R" and visit[i + 1][j + 1] != 1:
                i += 1
                j += 1
                visit[i + 1][j + 1] = 1
            elif pos5 == "R" and visit[i+1][j]!= 1:
                i += 1
                visit[i+1][j] = 1
print(visit)