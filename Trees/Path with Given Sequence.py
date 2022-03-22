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

def path(root,lis,i):
    if root==None:
        return False
    if root.data != lis[i] or i>len(lis):
        return False
    if root.left==None and root.right==None and root.data==lis[i]:
        return True
    return path(root.left,lis,i+1) or path(root.right,lis,i+1)
a=userInput()
print(path(a,[4,8,9],0))
