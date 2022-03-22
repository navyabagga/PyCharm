def replace(string,a,b):
    if len(string)==0:
        return ""
    if string[0]==a:
        return b+replace(string[1:],a,b)
    else:
        return string[0]+replace(string[1:],a,b)
string=str(input())
a=str(input())
b=str(input())
print(replace(string,a,b))