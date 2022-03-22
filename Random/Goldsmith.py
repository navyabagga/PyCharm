def maxlis(h):
    stack = list()
    max_area = 0
    index = 0
    while index < len(h):
        if (not stack) or (h[stack[-1]] <= h[index]):
            stack.append(index)
            index += 1
        else:
            top_of_stack = stack.pop()
            area = (h[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index))
            max_area = max(max_area,(h[top_of_stack] *
                    ((index - stack[-1] - 1)
                     if stack else index)))
    while stack:
        top_of_stack = stack.pop()
        area = (h[top_of_stack] *
                ((index - stack[-1] - 1)
                 if stack else index))
        max_area = max(max_area, area)
    return max_area


g=int(input())
b,h=map(int,input().split())
lis=list(map(int,input().split()))
s1=maxlis(lis)
s2=sum(lis)
print((s2-s1)*b*h)