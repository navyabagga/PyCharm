def power(x,y):
    if y==0:
        return 1
    else:
        return x* power(x,y-1)
x,y=map(int,input().split())
print(power(x,y))