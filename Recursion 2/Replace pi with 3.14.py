def replace(string,a,b):
    if len(string)==0 or len(string)==1:
        return string
    if string[0]=="p" and string[1]=="i":
        return b+replace(string[2:],a,b)
    else:
        return string[0]+replace(string[1:],a,b)
string=str(input())
a="pi"
b="3.14"
print(replace(string,a,b))