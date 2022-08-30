
def build_graph(edges, n):
    graph = {}

    for i in range(n):
        graph[i] = []

    for edge in edges:
        source = edge[0]
        destination = edge[1]

        graph[source].append(destination)
#         graph[destination].append(source)

    return graph

def display_graph(graph):
    for vertex in graph:
        print(str(vertex)+" -->", end = " ")
        print(*graph[vertex])

n = 5
edges = [[0, 1], [0, 2], [0, 4], [1, 2], [1, 3], [2, 3], [3, 4]]
graph = build_graph(edges, n)
display_graph(graph)