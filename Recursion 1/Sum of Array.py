def sum_array(lis):
    if len(lis)==0:
        return 0
    x=lis[0]+sum_array(lis[1:])
    return x
lis=list(map(int,input().split()))
print(sum_array(lis))