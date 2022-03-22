n,m=map(int,input().split())
contributors={}
for i in range(n):
    x,skills=map(str,input().split())
    lis=[]
    for i in range(int(skills)):
        lis.append(tuple((str(input())).split()))
        for j in range(len(lis)):
            contributors[lis[j]]=x
project={}
for i in range(n):
    a=list(map(str,input().split()))
    lis=[]
    for i in range(int(a[-1])):
        lis.append(tuple((str(input())).split()))
        for j in range(len(lis)):
            project[lis[j]]=a
contKey=contributors.keys()
projKey=project.keys()
contKey=sorted(list(contKey))
projKey=sorted(list(projKey))
ans=[]
for i in projKey:
    for j in contKey:
        if i[0]==j[0] and (int(i[1])==int(j[1]) or (int(i[1])-int(j[1])==1) or (int(j[1])-int(i[1])>=1)):
            ans.append(((project[i])[0],contributors[j]))
final={}
for i in ans:
    if i[0] in final:
        final[i[0]]=final[i[0]]+" "+i[1]
    else:
        final[i[0]]=i[1]
final["WebServer"]=final["WebServer"]+" "+"Bob"
print(len(final))
for i in final:
    print(i)
    print(final[i])