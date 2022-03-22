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
    if root==None:
        return bfs
    queue=deque([])
    queue.append(root)
    d=0
    while len(queue)!=0:
        lsize=len(queue)
        d+=1
        for i in range(lsize):
            c=queue.popleft()
            if c.left == None and c.right == None:
                return d
            if c.left!=None:
                queue.append(c.left)
            if c.right!=None:
                queue.append(c.right)
    return d
a=userInput()
print(BFS(a))