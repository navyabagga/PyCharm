import math
def insert(intervals, new_interval):
    intervals.append(new_interval)
    intervals.sort()
    print(intervals)
    start=intervals[0][0]
    end=intervals[0][1]
    ans=[]
    for i in intervals:
        print(i)
        if i[0] <= end:
            end=max(i[1], end)
        else:
            ans.append([start,end])
            start=i[0]
            end=i[1]
    ans.append([start,end])
    return ans
n=int(input())
interval=[]
for i in range(n):
    lis=[]
    lis.append(int(input()))
    lis.append(int(input()))
    interval.append(lis)
inter=[]
inter.append(int(input()))
inter.append(int(input()))
print(insert(interval,inter))
