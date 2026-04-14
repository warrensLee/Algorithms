from typing import List, Callable
from linked_list import LinkedList


class Graph:
    def __init__(self, n: int):
        self.n = n
        self.e: List[LinkedList] = [LinkedList() for _ in range(n)]
        self.reset()

    def reset(self) -> None:
        self.visited: List[bool] = [False] * self.n
        self.traces: List[int] = [-1] * self.n
        self.dist: List[int] = [1000000000] * self.n

    def distance(self, u: int) -> int:
        return self.dist[u]

    def set_distance(self, u: int, val: int) -> None:
        self.dist[u] = val

    def isVisited(self, u: int) -> bool:
        return self.visited[u]

    def setVisited(self, u: int) -> None:
        self.visited[u] = True

    def trace(self, u: int) -> int:
        return self.traces[u]

    def setTrace(self, u: int, v: int) -> None:
        self.traces[u] = v

    def insertEdge(self, u: int, v: int, w: int, directed: bool = False) -> None:
        self.e[u].insert((v, w))
        if not directed:
            self.e[v].insert((u, w))

    def search(self, start: int, destination: int, searchfn: Callable[['Graph', int, int], None]) -> List[int]:
        searchfn(self, start, destination)
        path: List[int] = []
        u = destination
        while u != -1:
            path.append(u)
            u = self.trace(u)
        path.reverse()
        return path
