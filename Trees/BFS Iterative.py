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
def BFS(root):
    bfs=[]
    if root==None:
        return bfs
    queue=deque([])
    queue.append(root)
    while len(queue)!=0:
        lsize=len(queue)
        curr=[]
        for i in range(lsize):
            c=queue.popleft()
            curr.append(c.data)
            if c.left!=None:
                queue.append(c.left)
            if c.right!=None:
                queue.append(c.right)
        bfs.append(curr)
    return bfs
a=userInput()
print(BFS(a))