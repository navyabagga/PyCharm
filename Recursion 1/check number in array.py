def check(lis,num):
    if len(lis)==0:
        return "False"
    if lis[0]==num:
        return "True"
    else:
        return check(lis[1:],num)
lis=list(map(int,input().split()))
num=int(input())
print(check(lis,num))
