# creating graph using adjecancy matrix

def build_graph(edges ):
    matrix = [[0]*len(edges) for i in range(len(edges))]

    for edge in edges:
        source = edge[0]
        destination = edge[1]

        matrix[source][destination] = 1
        matrix[destination][source] = 1

    return matrix

def display_graph(graph):
    for row in range(len(graph)):
        for column in range(len(graph[0])):
            print(graph[row][column], end = " | ")
        print("\n---------------------------")

edges = [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3], [2, 3], [3, 4]]
# s=set()
# for i in edges:
#     s.add(i[0])
#     s.add(i[1])
graph = build_graph(edges)
display_graph(graph)

# ------------------------------------------
# creating graph using adjaceny list

# def build_graph(edges, n):
#     graph = {}
#
#     for i in range(n):
#         graph[i] = []
#
#     for edge in edges:
#         source = edge[0]
#         destination = edge[1]
#
#         graph[source].append(destination)
# #         graph[destination].append(source)
#
#     return graph
#
# def display_graph(graph):
#     for vertex in graph:
#         print(str(vertex)+" -->", end = " ")
#         print(*graph[vertex])
#
# n = 5
# edges = [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3], [2, 3], [3, 4]]
# graph = build_graph(edges, n)
# display_graph(graph)
# -----------------------------------
# class graph:
#     def _init_(self,gdict=None):
#         if gdict == None:
#             gdict = {}
#         self.gdict = gdict
#
#     #to print vertices
#     def displayvertex(self):
#         return list(self.gdict.keys())
#
#     #to print edges
#     def displayedges(self):
#         edgelist = []
#         for vertex1 in self.gdict.keys():
#             for vertex2 in self.gdict[vertex1]:
#                 if [vertex1,vertex2] not in edgelist:
#                     edgelist.append([vertex1,vertex2])
#                 else:
#                     continue
#         return edgelist
#
#     #to add vertex
#     def addvertex(self, newvertex):
#         self.newvertex = newvertex
#         if self.newvertex not in self.gdict.keys():
#             self.gdict[self.newvertex] = []
#
#     #to add edge
#     def addedge(self, newedge):
#         self.newedge = newedge
#         vertex1,vertex2 = self.newedge
#         if vertex1 in self.gdict:
#             self.gdict[vertex1].append(vertex2)
#         else:
#             self.gdict[vertex1] = [vertex2]
#
#
#
# graph_elements = { "a" : ["b","c"],"b" : ["a", "d"],"c" : ["a", "d"],"d" : ["b","c","e"],"e" : ["d"] }
# obj = graph(graph_elements)
# print(obj.displayvertex())
# print(obj.displayedges())
# obj.addvertex("f")
# obj.addedge(["e","f"])
# print(obj.displayvertex())
# print(obj.displayedges())
# -------------------
# DFS
# def build_graph(v, edges):
#     graph = {}
#     for i in range(v):
#         graph[i] = []
#
#     for edge in edges:
#         parent = edge[0]
#         child = edge[1]
#
#         graph[parent].append(child)
#         graph[child].append(parent)
#
#     return graph
#
# def dfs_exe(start, graph, visited, ans):
#     visited[start] = True
#     ans.append(start)
#
#     for node in graph[start]:
#         if visited[node] is not True:
#             dfs_exe(node, graph, visited, ans)
#
#
# def dfs(v, edges):
#     visited = [False]*v
#     ans = []
#     graph = build_graph(v, edges)
#     dfs_exe(0, graph, visited, ans)
#     return ans
#
# v = 7
# edges = [[6,4],[6,2],[5,3],[5,4],[3,0],[3,1],[3,2],[4,1],[0,5]]
# ans = dfs(v, edges)
# print(ans)

# ---------------------------------------
# BFS
# def build_graph(v, edges):
#     graph = {}
#     for i in range(v):
#         graph[i] = []
#
#     for edge in edges:
#         parent = edge[0]
#         child = edge[1]
#
#         graph[parent].append(child)
#         graph[child].append(parent)
#
#     return graph
#
# def dfs_exe(start, graph, visited, ans, que):
#     visited[start] = True
#     que.insert(0, start)
#
#     while que:
#         vertex = que.pop(0)
#         ans.append(vertex)
#
#         for node in graph[vertex]:
#             if visited[node] is not True:
#                 visited[node] = True
#                 que.append(node)
#
#
# def bfs(v, edges):
#     visited = [False]*v
#     que = []
#     ans = []
#     graph = build_graph(v, edges)
#     dfs_exe(1, graph, visited, ans, que)
#     return ans
#
# # v = 7
# # edges = [[6,4],[6,2],[5,3],[5,4],[3,0],[3,1],[3,2],[4,1],[0,5]]
# # edges = [[0,1], [0,2], [0,3], [1,2], [2,4]]
# v = 5
# edges = [[1,2],[1,3],[3,4]]
# ans = bfs(v, edges)
# print(ans)

# -------------------------------------------------
# topological ordering
# def topological(v, edges):
#     ans = []
#     if v<=0:
#         return ans
#
#     graph = {}
#     for i in range(v):
#         graph[i] = []
#
#     indegree = {}
#     for i in range(v):
#         indegree[i] = 0
#
#     for edge in edges:
#         parent = edge[0]
#         child = edge[1]
#         indegree[child] += 1
#         graph[parent].append(child)
#
#     que = []
#     for i in indegree:
#         if indegree[i] == 0:
#             que.append(i)
#
#     while que:
#         node = que.pop(0)
#         ans.append(node)
#
#         for neighb in graph[node]:
#             indegree[neighb] -= 1
#
#             if indegree[neighb] == 0:
#                 que.append(neighb)
#
#     if len(ans)!=v:
#         return []
#
#     return ans
#
# v = 7
# edges = [[5, 3], [5, 4], [6, 4], [6, 2], [4, 1], [3, 0], [3, 1], [3, 2]]
# ans = topological(v, edges)
# print(ans)

# ------------------------
# prim's algorithm

# def find_source(distance, mstset, v):
#     min_val = float("inf")
#     index = 0
#     for source in range(v):
#         if distance[source] < min_val and mstset[source] == False: #to find the vertex that has minimum distance
#             min_val = distance[source]
#             index = source
#     return index
#
# def printMST(parent, distance):
#     print ("Edge \tWeight")
#     for i in range(1, v):
#         if parent[i] != None:
#             print (parent[i], "->", i, "\t", distance[i])
#
# def prim(v, matrix):
#     distance = [float("inf")]*v
#     mstset = [False]*v
#     parent = [None]*v
#
#     distance[0] = 0
#     parent[0] = -1
#
#     for vertex in range(v): # do this process the number of vertex times
#         source = find_source(distance, mstset, v)
#         mstset[source] = True
#         for neighbor in range(v):
#             if matrix[source][neighbor]>0 and mstset[neighbor] == False and distance[neighbor] > matrix[source][neighbor]:
#                 distance[neighbor] = matrix[source][neighbor]
#                 parent[neighbor] = source
#     printMST(parent, distance)
#
# v = 5
# # matrix = [[0, 4, 6, 0, 0, 0],
# #           [4, 0, 6, 3, 4, 0],
# #           [6, 6, 0, 1, 0, 0],
# #           [0, 3, 1, 0, 2, 3],
# #           [0, 4, 0, 2, 0, 7],
# #           [0, 0, 0, 3, 7, 0]]
#
# matrix = [[0, 0, 3, 0, 0],
#           [0, 0, 10, 4, 0],
#           [3, 10, 0, 2, 6],
#           [0, 4, 2, 0, 1],
#           [0, 0, 6, 1, 0]]
#
# # matrix = [ [0, 2, 0, 6, 0],
# #             [2, 0, 3, 8, 5],
# #             [0, 3, 0, 0, 7],
# #             [6, 8, 0, 0, 9],
# #             [0, 5, 7, 9, 0]]
#
# ans = prim(v, matrix)
# # print(ans)

# ------------------------------------
# Dijkstra algorithm

# from heapq import *
#
#
# def build_graph(v, edges):
#     graph = {}
#     for i in range(1, v + 1):
#         graph[i] = []
#
#     for edge in edges:
#         graph[edge[0]].append(edge[1])
#
#     return graph
#
#
# def build_cost(v, edges):
#     cost = {}
#     for edge in edges:
#         cost[(edge[0], edge[1])] = edge[2]
#
#     return cost
#
#
# def dijkstra(v, edges):
#     graph = build_graph(v, edges)
#     distance = [float("inf")] * (v + 1)
#     parent = [-1] * (v + 1)
#     visited = [False] * (v + 1)
#     cost = build_cost(v, edges)
#     min_heap = []
#
#     src = 1
#     heappush(min_heap, (0, src))
#     distance[src] = 0
#
#     while min_heap:
#         curr_distance, curr_node = heappop(min_heap)
#         if visited[curr_node] is False:
#             visited[curr_node] = True
#             for nbr in graph[curr_node]:
#                 if distance[nbr] > curr_distance + cost[(curr_node, nbr)]:
#                     distance[nbr] = curr_distance + cost[(curr_node, nbr)]
#                     parent[nbr] = curr_node
#                     heappush(min_heap, (distance[nbr], nbr))
#
#     print("Edge \tWeight")
#     for i in range(1, v + 1):
#         print(parent[i], "->", i, "\t", distance[i])
#
#
# v = 4
# edges = [[1, 2, 2], [1, 3, 9], [1, 4, 14], [1, 3, 9], [3, 4, 2]]
# dijkstra(v, edges)

# -------------------------------------------------
# adjacancy matrix, adjacancy list, bfs, dfs, prim's algorithm, dijkstra algorithm, topological ordering.
# kruskal's algorithm, floyd warshel's algorithm, belmen ford algorithm, tsp