class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
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
def leafNodes(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return 1
    l=leafNodes(root.left)
    r=leafNodes(root.right)
    return l+r
a=userInput()
print(leafNodes(a))
