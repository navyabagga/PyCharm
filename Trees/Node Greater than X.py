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
def greaterThanX(root,lis,X):
    if root == None:
        return -1
    l=greaterThanX(root.left,lis,X)
    r=greaterThanX(root.right,lis,X)
    if root.data>X:
        lis.append(root.data)
    return lis
a=treeInput()
X=int(input())
print(greaterThanX(a,[],X))
