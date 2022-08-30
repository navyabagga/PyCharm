def find_source(distance, mstset, v):
    min_val = float("inf")
    index = 0
    for source in range(v):
        if distance[source] < min_val and mstset[source] == False: #to find the vertex that has minimum distance
            min_val = distance[source]
            index = source
    return index

def printMST(parent, distance):
    print ("Edge \tWeight")
    for i in range(1, v):
        if parent[i] != None:
            print (parent[i], "->", i, "\t", distance[i])

def prim(v, matrix):
    distance = [float("inf")]*v
    mstset = [False]*v
    parent = [None]*v

    distance[0] = 0
    parent[0] = -1

    for vertex in range(v): # do this process the number of vertex times
        source = find_source(distance, mstset, v)
        mstset[source] = True
        for neighbor in range(v):
            if matrix[source][neighbor]>0 and mstset[neighbor] == False and distance[neighbor] > matrix[source][neighbor]:
                distance[neighbor] = matrix[source][neighbor]
                parent[neighbor] = source
    printMST(parent, distance)

v = 5
# matrix = [[0, 4, 6, 0, 0, 0],
#           [4, 0, 6, 3, 4, 0],
#           [6, 6, 0, 1, 0, 0],
#           [0, 3, 1, 0, 2, 3],
#           [0, 4, 0, 2, 0, 7],
#           [0, 0, 0, 3, 7, 0]]

matrix = [[0, 0, 3, 0, 0],
          [0, 0, 10, 4, 0],
          [3, 10, 0, 2, 6],
          [0, 4, 2, 0, 1],
          [0, 0, 6, 1, 0]]

# matrix = [ [0, 2, 0, 6, 0],
#             [2, 0, 3, 8, 5],
#             [0, 3, 0, 0, 7],
#             [6, 8, 0, 0, 9],
#             [0, 5, 7, 9, 0]]

ans = prim(v, matrix)
# print(ans)
