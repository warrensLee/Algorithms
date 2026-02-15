from graph import Graph
from queue import Queue


def bfs(g: Graph, start: int, destination: int) -> None:
    queue: Queue[int] = Queue()
    g.reset()
    # YOUR CODE HERE
    while not queue.empty():
        u = queue.pop()
        # YOUR CODE HERE
        number_of_adjacency_nodes = g.e[u].size()
        p = g.e[u].get_root()
        for _ in range(number_of_adjacency_nodes):
            v = p.value
            # YOUR CODE HERE
            p = p.next
