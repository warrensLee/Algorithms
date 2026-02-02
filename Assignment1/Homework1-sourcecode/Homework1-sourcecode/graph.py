from linked_list import LinkedList
from queue import Queue


class Graph:
    def __init__(self, n):
        self.n = n
        self.e = [LinkedList() for _ in range(n)]

    def insert_edge(self, u, v, directed=False):
        self.e[u].insert(v)
        if not directed:
            self.e[v].insert(u)

    def search(self, start, destination):
        queue = Queue()
        mask = [0] * self.n
        trace = [-1] * self.n
        queue.push(start)
        mask[start] = 1

        while not queue.empty():
            u = queue.pop()
            if u == destination:
                break
            for v in self.e[u]:
                if mask[v] == 0:
                    queue.push(v)
                    trace[v] = u
                    mask[v] = 1

        path = []
        u = destination
        while u != -1:
            path.append(u)
            u = trace[u]
        path.reverse()
        return path
