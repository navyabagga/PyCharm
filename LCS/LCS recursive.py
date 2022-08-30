def LCS(s1,s2,n,m):
    if n==0 or m==0:
        return 0
    elif s1[n-1]==s2[m-1]:
        return LCS(s1,s2,n-1,m-1)+1
    else:
        return max(LCS(s1,s2,n-1,m),LCS(s1,s2,n,m-1))
a="abcdab"
b="bdcaba"
print(LCS(a,b,len(a),len(b)))
