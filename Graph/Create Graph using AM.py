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