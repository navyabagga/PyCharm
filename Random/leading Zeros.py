#given a number find all binary strings of len n and calculate how many strings do not have leading zeros
#       0   1   2   3   4   5   6
#0's    0   1   1   2   3   5   8
#1's    0   1   2   3   5   8   13
n=int(input())
zero=1
one=1
for i in range(2,n+1):
    p=zero
    zero=one
    one=p+one
print(zero+one)