import math
#negative weights included
def bellman_ford(vertices,edges,src):
    # array storing distance bw two nodes after relaxing
    distance=[math.inf]*(vertices+1)
    # distance from starting point to starting point
    distance[src]=0
    # run loop for vertices-1 time to find best possible and
    for i in range(vertices-1):
        for edge in edges:
            src,dest,weight=edge[0],edge[1],edge[2]
            if distance[src]+weight<distance[dest]:
                distance[dest]=distance[src]+weight
    print(distance)
if __name__=="__main__":
    vertices=5
    # [a,b,c]
    # a=Staring point
    # b=Ending Point
    # c=Weight of moving from a to b
    edges=[[0,1,-1],[0,2,4],[1,2,3],[1,3,2],[1,4,2],[3,2,5],[3,1,1],[4,3,-3]]
    bellman_ford(vertices,edges,1)
