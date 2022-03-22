def sort(lis):
    if len(lis)==1 or len(lis)==0:
        return True
    if lis[0]>lis[1]:
        return False
    x=sort(lis[1:])
    return x

lis=list(map(int,input().split()))
print(sort(lis))