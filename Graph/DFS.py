def build_graph(v, edges):
    graph = {}
    for i in range(v):
        graph[i] = []

    for edge in edges:
        parent = edge[0]
        child = edge[1]

        graph[parent].append(child)
        graph[child].append(parent)

    return graph

def dfs_exe(start, graph, visited, ans):
    visited[start] = True
    ans.append(start)

    for node in graph[start]:
        if visited[node] is not True:
            dfs_exe(node, graph, visited, ans)


def dfs(v, edges):
    visited = [False]*v
    ans = []
    graph = build_graph(v, edges)
    dfs_exe(0, graph, visited, ans)
    return ans

v = 7
edges = [[6,4],[6,2],[5,3],[5,4],[3,0],[3,1],[3,2],[4,1],[0,5]]
ans = dfs(v, edges)
print(ans)