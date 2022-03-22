def fib(n):
    lis=[0 for i in range(n+1)]
    lis[1]=1
    for i in range(2,len(lis)):
        lis[i]=lis[i-1]+lis[i-2]
    print(liStra