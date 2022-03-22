def print_n(n):
    if n==1:
        print("1")
    else:
        print(n)
        print_n(n-1)
n=int(input())
print(print_n(n))