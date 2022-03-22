from collections import deque
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


def BFS(root,n):
    if root==None:
        return None
    queue=deque([])
    queue.append(root)
    while len(queue) !=0:
        c=queue.popleft()
        if c.left!=None:
            queue.append(c.left)
        if c.right!=None:
            queue.append(c.right)
        if c.data==n:
            break
    return queue.popleft().data
a=userInput()
n=int(input())
print(BFS(a,n))