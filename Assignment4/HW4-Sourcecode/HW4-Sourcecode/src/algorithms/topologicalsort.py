from typing import List
from graph import Graph

def topological_sort(graph: Graph) -> List[int]:
    # Get the number of vertices in the graph
    n = graph.get_n()

    # Initialize in-degree array (number of incoming edges for each vertex)
    in_degree = [0] * n

    # for every vertex u
        # for each outgoing edge from u
    for u in range(n):
        for edge in graph.e[u]:
            in_degree[edge.v] += 1    

    
    # go thru each node and add them
    # to the stack if in_degree = 0
    stack = []
    for i in range(n):
        if in_degree[i] == 0:
            stack.append(i)

    # final topological order (result)
    order = []

    # go thru all nodes w/ in_degree = 0
    while stack:
        u = stack.pop()
        order.append(u)
        
        # all nodes v that connect in direction towards u
        for edge in graph.e[u]:
            v = edge.v
            in_degree[v] -= 1

            # if v has no incoming edges
            if in_degree[v] == 0:
                stack.append(v)

    # if all nodes were not checked
    #  (meaning there is a cycle)
    if len(order) != n:
        return []
    else:
        return order

