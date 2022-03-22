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
def sumNode(root):
    if root == None:
        return 0
    l=sumNode(root.left)
    r=sumNode(root.right)
    return root.data+l+r
a=treeInput()
print(sumNode(a))