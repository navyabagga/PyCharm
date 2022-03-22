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
    ltr=True
    if root==None:
        return bfs
    queue=deque([])
    queue.append(root)
    while len(queue)!=0:
        lsize=len(queue)
        curr=deque()
        for i in range(lsize):
            c=queue.popleft()
            if ltr==True:
                curr.append(c.data)
            else:
                curr.appendleft(c.data)
            if c.left!=None:
                queue.append(c.left)
            if c.right !=None:
                queue.append(c.right)
        bfs.append(list(curr))
        ltr=not ltr
    return bfs
a=userInput()
print(BFS(a))