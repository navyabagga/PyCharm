def fib(n,d):
    if n in d:
        return d[n]
    else:
        if n-1 in d:
            ans1=d[n-1]
        else:
            ans1=fib(n-1,d)
            d[n-1]=ans1
        if n-2 in d:
            ans2=d[n-2]
        else:
            ans2=fib(n-2,d)
            d[n-2]=ans2
        return ans1+ans2
n=int(input())
d={0:0,1:1}
print(fib(n-1,d))
print(d)