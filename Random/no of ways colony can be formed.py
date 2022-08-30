import math
n=int(input())
building=1
space=1
for i in range(2,n+1):
    p=building
    building=space
    space=p+space
print(int(math.pow(building+space,2)))