class Node:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None
n1=Node(int(input()))
n2=Node(int(input()))
n3=Node(int(input()))
n1.left=n2
n1.right=n3
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
print(printTree(n1))