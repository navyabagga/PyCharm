from collections import deque
G = []
def treeCut(n, k, edges):
    G[:] = [[] for _ in range(n)]
    for i in range(n - 1):
        G[edges[i][0] - 1].append(edges[i][1] - 1)
        G[edges[i][1] - 1].append(edges[i][0] - 1)
    def bfs(s):
        distances = [n for i in range(n)]
        for i in s:
            distances[i] = 0
        q = deque(s)
        while q:
            u = q.popleft()
            for v in G[u]:
                if distances[v] > 1 + distances[u]:
                    distances[v] = 1 + distances[u]
                    q.append(v)
        return distances
    ans = 1e9
    i=0
    while i<n:
        d = bfs([i])
        d.sort()
        ans = min(ans, d[n - k - 1] * 2)
        i+=1
    i=0
    while i<n - 1):
        d = bfs([edges[i][0] - 1, edges[i][1] - 1])
        d.sort()
        ans = min(ans, d[n - k - 1] * 2 + 1)
    return ans
n=int(input())
k=int(input())


print(treeCut(3,0,[[1,2],[1,3]]))