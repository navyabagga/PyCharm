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
def printTree(root):
    if root == None:
        return
    print(root.data,end=" : ")
    if root.left != None:
        print("L",root.left.data, end=",")
    if root.right != None:
        print("R",root.right.data, end="")
    print()
    printTree(root.left)
    printTree(root.right)
a=treeInput()
printTree(a)
