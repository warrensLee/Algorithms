from dataclasses import dataclass
from typing import List


@dataclass
class Edge:
    u: int = 0
    v: int = 0
    w: int = 0


class Graph:
    def __init__(self, n: int):
        self.n = n
        self.e: List[List[Edge]] = [[] for _ in range(n)]
        self.reset()

    def export_edges(self) -> List[Edge]:
        edges: List[Edge] = []
        for u in range(self.n):
            for edge in self.e[u]:
                edges.append(Edge(edge.u, edge.v, edge.w))
        return edges

    def reset(self) -> None:
        self.visited = [False] * self.n
        self.traces = [-1] * self.n
        self.dist = [10**9] * self.n

    def distance(self, u: int) -> int:
        return self.dist[u]

    def is_visited(self, u: int) -> bool:
        return self.visited[u]

    def set_visited(self, u: int) -> None:
        self.visited[u] = True

    def trace(self, u: int) -> int:
        return self.traces[u]

    def set_trace(self, u: int, v: int) -> None:
        self.traces[u] = v

    def insert_edge(self, u: int, v: int, w: int, directed: bool = False) -> None:
        self.e[u].append(Edge(u, v, w))
        if not directed:
            self.e[v].append(Edge(v, u, w))

    def get_n(self) -> int:
        return self.n

    def search(self, start: int, destination: int):
        from algorithms.dijkstra import search_shortest_path

        return search_shortest_path(self, start, destination)
