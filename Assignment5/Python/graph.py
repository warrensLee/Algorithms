from collections import deque


class Graph:
    def __init__(self, nodes):
        self.n = nodes
        self.adj = [[] for _ in range(self.n)]
        # Adjacency matrix initialized to INF for Floyd-Warshall compatibility
        self.adjMatrix = [[int(1e9) for _ in range(self.n)] for _ in range(self.n)]
        for i in range(self.n):
            self.adjMatrix[i][i] = 0

    def insertEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)  # Assuming undirected for campus map
        self.adjMatrix[u][v] = 1
        self.adjMatrix[v][u] = 1

    def search(self, start, end):
        if start == end:
            return [start]

        q = deque()
        parent = [-1] * self.n
        visited = [False] * self.n

        q.append(start)
        visited[start] = True

        while q:
            u = q.popleft()
            if u == end:
                break

            for neighbor in self.adj[u]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    parent[neighbor] = u
                    q.append(neighbor)

        path = []
        v = end
        while v != -1:
            path.append(v)
            v = parent[v]
        path.reverse()

        if len(path) == 1 and path[0] != start:
            return []  # No path found
        return path

    # Helper for algorithms.py
    def getDistanceMatrix(self):
        return [row[:] for row in self.adjMatrix]
