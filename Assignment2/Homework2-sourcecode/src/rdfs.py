from graph import Graph


def rdfs(g: Graph, start: int, destination: int) -> None:
    # YOUR CODE HERE
    number_of_adjacency_nodes = g.e[start].size()
    p = g.e[start].get_root()
    for _ in range(number_of_adjacency_nodes):
        v = p.value
        # YOUR CODE HERE
        p = p.next
