def check(lis,num,x):
    if len(lis)==0:
        return "Element Not Present"
    if lis[len(lis)-1]==num:
        return x
    else:
        return check(lis[:len(lis)-1],num,x-1)
lis=list(map(int,input().split()))
num=int(input())
x=len(lis)
print(check(lis,num,x))
