from graph import Graph

# Recursive Depth-First Search (RDFS)
# Explores the graph by going as deep as possible along each branch before backtracking.
# Uses recursion (implicit call stack) instead of an explicit stack.
# A shared visited set prevents cycles and repeated work.
# g.set_trace(v, u) records parent relationships so the final path can be reconstructed.
# The helper function returns True when the destination is found,
# allowing the success to propagate upward and stop further exploration early.


def rdfs(g: Graph, start: int, destination: int) -> None:
    g.reset()
    # establish visited set and start the recursive call of rdfs
    _rdfs(g, start, destination)


def _rdfs(g: Graph, u: int, destination: int) -> bool:
    # stop if this node has already been visited (prevents cycles)
    if g.is_visited(u):
        return False
    # add to visited set
    g.set_visited(u)

    # if destination is reached, return True to stop further exploration
    if u == destination:
        return True
    
    # gets the number of neighbors to u
    number_of_adjacency_nodes = g.e[u].size()
    p = g.e[u].get_root()
    # gets the head of u's adjacency list

    for _ in range(number_of_adjacency_nodes):
        v = p.value
        # v is one neighbor of u
        if not g.is_visited(v):
            # record u as the parent of v for path reconstruction
            g.set_trace(v, u)
            # if recursive call finds destination, propagate True upward
            if _rdfs(g, v, destination):
                return True
        p = p.next

    return False