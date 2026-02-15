from graph import Graph
from stack import Stack


def dfs(g: Graph, start: int, destination: int) -> None:
    stack: Stack[int] = Stack()
    g.reset()
    # YOUR CODE HERE
    while not stack.empty():
        u = stack.pop()
        # YOUR CODE HERE
        number_of_adjacency_nodes = g.e[u].size()
        p = g.e[u].get_root()
        for _ in range(number_of_adjacency_nodes):
            v = p.value
            # YOUR CODE HERE
            p = p.next
