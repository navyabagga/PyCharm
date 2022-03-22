class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
def treeInput():
    r=int(input())
    if r==-1:
        return None
    root=Node(r)
    l=treeInput()
    r=treeInput()
    root.left=l
    root.right=r
    return root
def large(root,m):
    if root == None:
        return -1
    l=large(root.left,m)
    r=large(root.right,m)
    m=max(root.data,l,r)
    return m
a=treeInput()
print(large(a,float("-inf")))
