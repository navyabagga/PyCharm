from collections import deque
visited={}
level={}#distence between 2 node
parent={}
bfs_output=[]
queue=deque([])
adj_list={"A":["B","D"],"B":["A","C"],"C":["B"],"D":["A","E","F"],"E":["D","F","G"],"F":["D","E","H"],"G":["E","H"],"H":["G","F"]}
for node in adj_list.keys():
    visited[node]=False
    parent[node]=None
    level[node]=-1
s="A"
visited[s]=True
level[s]=0
queue.append(s)
while len(queue)!=0:
    u=queue.popleft()
    bfs_output.append(u)
    for v in adj_list[u]:
        if not visited[v]:
            visited[v]=True
            parent[v]=u
            level[v]=level[u]+1
            queue.append(v)
print(bfs_output)
#shortest path from any node to source node
v="G"
path=[]
while v is not None:
    path.append(v)
    v=parent[v]
path=path[::-1]
print(path)