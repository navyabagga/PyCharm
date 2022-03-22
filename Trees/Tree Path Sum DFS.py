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

def pathSum(root,psum):
    if root==None:
        return 0
    psum = psum*10+root.data
    if root.left==None and root.right==None:
        return psum
    else:
        return pathSum(root.left,psum)+pathSum(root.right,psum)
a=userInput()
print(pathSum(a,0))