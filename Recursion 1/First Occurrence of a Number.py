def check(lis,num,x):
    if len(lis)==0:
        return "Element Not Present"
    if lis[0]==num:
        return x
    else:
        return check(lis[1:],num,x+1)
lis=list(map(int,input().split()))
num=int(input())
x=1
print(check(lis,num,x))
