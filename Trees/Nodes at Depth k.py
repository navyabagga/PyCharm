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
def depthK(root,k,lis):
    if root==None:
        return
    if k==0:
        lis.append(root.data)
        return
    depthK(root.left,k-1,lis)
    depthK(root.right,k-1,lis)
    return lis
a=userInput()
k=int(input())
print(depthK(a,k,[]))
