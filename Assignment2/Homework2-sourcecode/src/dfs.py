from graph import Graph
from stack import Stack


# Depth-First Search (DFS)
# Uses a stack (LIFO) to explore as deep as possible before backtracking.
# visited prevents cycles.
# g.set_trace(v, u) records the parent of v for path reconstruction.


def dfs(g: Graph, start: int, destination: int) -> None:
    stack: Stack[int] = Stack()
    g.reset()
    # push the first node and add that to the visited set()
    stack.push(start)
    g.set_visited(start)

    # while stack is valid (not empty)
    while not stack.empty():
        # get the node of the graph being investigated and store its information as u
        u = stack.pop()

        # now if u happens to be where we need to be lets return!
        if u == destination:
            return
        
        # adjacent nodes is = to graph edge[u]'s size
        number_of_adjacency_nodes = g.e[u].size()
        # p will be the root of this graph and serve as a point of traversal
        p = g.e[u].get_root()
        # traverse through each adjacent node
        for _ in range(number_of_adjacency_nodes):
            v = p.value
            # if this node had not been visited
            if not g.is_visited(v):
                g.set_visited(v)
                # make graph trace between v and u (current node and the last node)
                g.set_trace(v, u)       
                # add v to the stack to be explored later
                stack.push(v)

            p = p.next
