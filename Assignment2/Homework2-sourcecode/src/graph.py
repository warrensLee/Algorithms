from typing import Callable, List
from linked_list import LinkedList


class Graph:
    def __init__(self, n: int) -> None:
        self.n = n
        self.e: List[LinkedList[int]] = [LinkedList() for _ in range(n)]
        self.reset()

    def reset(self) -> None:
        self.visited = [False] * self.n
        self.traces = [-1] * self.n

    def is_visited(self, u: int) -> bool:
        return self.visited[u]

    def set_visited(self, u: int) -> None:
        self.visited[u] = True

    def trace(self, u: int) -> int:
        return self.traces[u]

    def set_trace(self, u: int, v: int) -> None:
        self.traces[u] = v

    def insert_edge(self, u: int, v: int, directed: bool = False) -> None:
        self.e[u].insert(v)
        if not directed:
            self.e[v].insert(u)

    def search(self, start: int, destination: int, searchfn: Callable[["Graph", int, int], None]) -> List[int]:
        searchfn(self, start, destination)

        path: List[int] = []
        u = destination
        while u != -1:
            path.append(u)
            u = self.trace(u)

        path.reverse()
        return path
