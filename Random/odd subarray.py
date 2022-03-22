st=str(input())
lis=list(map(int,st.split(" ")))
finlis=[]
for i in range(len(lis)):
    for j in range(i,len(lis)):
        finlis.append(lis[i:j+1])
count=0
print(finlis)
for i in finlis:
    if sum(i)%2!=0:
        count+=1
print(count)
