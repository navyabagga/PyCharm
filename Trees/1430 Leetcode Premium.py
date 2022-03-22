#Check if a string is a valid sequence from root to Leaf in a binary tree
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
def fun(root,lis,i):
    if root==None:
        return False
    if i>len(lis) or root.data!=lis[i]:
        return False
    if root.left==None and root.right==None and root.data==lis[i]:
        return True
    return fun(root.left,lis,i+1) or fun(root.right,lis,i+1)


r=userInput()
lis=list(map(int,input().split()))
print(fun(r,lis,0))