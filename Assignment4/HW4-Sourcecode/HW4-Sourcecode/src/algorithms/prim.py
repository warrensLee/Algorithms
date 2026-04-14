from typing import List
import heapq

from graph import Edge, Graph

def construct_mst_prim(G: Graph) -> List[Edge]:
    edges = G.export_edges()  # Graph's edges (may include both directions)
    n = G.get_n()
    mst: List[Edge] = []
    heap: List[tuple[int, int, int, Edge]] = []
    # you can use heap to optimize the minimum searching

    # return if there are 0 vertices
    # create a set to track what nodes
    # have and have not been seen
    if n == 0: return mst
    visited = [False] * n

    # for step one we must
    # visit vertex 0 and set
    # push all edges into min-heap
    visited[0] = True
    for edge in G.e[0]:
        heapq.heappush(heap, (edge.w, edge.u, edge.v, edge))

    # add smallest valid edge repeating
    # until the mst has n - 1 edges.
    while heap and len(mst) < n - 1:
        w, u, v, edge = heapq.heappop(heap)

        if visited[v]:
            continue

        # if unvisited add this edge
        mst.append(edge)
        visited[v] = True

        # push all edges from this new vertex
        for next_edge in G.e[v]:
            if not visited[next_edge.v]:
                heapq.heappush(heap, (next_edge.w, next_edge.u, next_edge.v, next_edge))
        
    # after the loop, check for
    # a disconnected graph to ensure
    # that MST can include all vertices
    if len(mst) != n - 1:
        return []

    return mst
