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
def preOrder(root,lis):
    if root == None:
        return
    lis.append(root.data)
    preOrder(root.left,lis)
    preOrder(root.right,lis)
    return lis
def postOrder(root,lis):
    if root == None:
        return
    postOrder(root.left,lis)
    postOrder(root.right,lis)
    lis.append(root.data)
    return lis
def inOrder(root,lis):
    if root == None:
        return
    inOrder(root.left,lis)
    lis.append(root.data)
    inOrder(root.right,lis)
    return lis
a=treeInput()
lis=[]
print(preOrder(a,lis))
lis=[]
print(postOrder(a,lis))
lis=[]
print(inOrder(a,lis))