class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def userInput():
    r=int(input())
    if r == -1:
        return None
    root=Node(r)
    l=userInput()
    r=userInput()
    root.left=l
    root.right=r
    return root
def heightOfTree(root):
    if root == None:
         return 0
    l=1+heightOfTree(root.left)
    r=1+heightOfTree(root.right)
    return max(l,r)
a=userInput()
print(heightOfTree(a))