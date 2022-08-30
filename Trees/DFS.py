class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def userInput():
    r=int(input())
    if r==-1:
        return None
    root=Node(r)
    l=userInput()
    r=userInput()
    root.left=l
    root.right=r
    return root
def find_height(root):
    if root is None:
        return 0
    leftHeight=find_height(root.left)
    rightHeight=find_height(root.right)
    dia=leftHeight+rightHeight+1
    diameter=max(find_height(leftHeight),find_height(rightHeight))
    return max(dia, diameter)+1
def diameter(root):
    diam=find_height(root)
    return diam
a=userInput()
print(diameter(a))
'''
3
4
6
-1
-1
-1
5
7
-1
-1
8
2
-1
-1
-1
'''