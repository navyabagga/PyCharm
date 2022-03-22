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
def countNodes(root):
    if root==None:
        return 0
    l=countNodes(root.left)
    r=countNodes(root.right)
    return 1+r+l
a=treeInput()
print(countNodes(a))