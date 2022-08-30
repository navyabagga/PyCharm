import re
lis=[]
for i in range(3):
    lis.append(str(input()))
drate={'RCB':0,'RR':0,'KKR':0,'CSK':0,'SRH':0,'MI':0,'DC':0,'PBKS':0}
dcount={'RCB':0,'RR':0,'KKR':0,'CSK':0,'SRH':0,'MI':0,'DC':0,'PBKS':0}
for i in lis:
    lis1=i.split()
    lis1[1] = re.split(r'/', lis1[1])
    lis1[4] = re.split(r'/', lis1[4])
    if int(lis1[1][0])==int(lis1[4][0]):
        dcount[lis1[0]] += 1
        dcount[lis1[3]]+=1
    elif int(lis1[1][0])>int(lis1[4][0]):
        diff=int(lis1[1][0])-int(lis1[4][0])
        rr=diff*0.05
        drate[lis1[0]]+=rr
        drate[lis1[3]]-=rr
        dcount[lis1[0]]+=2
    elif int(lis1[4][0]) > int(lis1[1][0]):
        projected=(int(lis1[4][0])/int(lis1[-1]))*120
        ans=(projected-int(lis1[1][0]))*0.05
        drate[lis1[0]]-=ans
        drate[lis1[3]]+=ans
        dcount[lis1[3]]+=2
print(dcount)
print(drate)
for i in dcount:
    dcount[i]=(dcount[i],drate[i])
print(dcount)
dcount=dict(sorted(dcount.items(), key=lambda item: item[1],reverse=True))
print(dcount)
k=dcount.keys()
print(list(k))