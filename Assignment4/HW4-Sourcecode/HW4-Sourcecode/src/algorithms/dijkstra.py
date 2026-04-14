import heapq
from typing import List

from graph import Graph

def search_shortest_path(G: Graph, start: int, destination: int) -> List[int]:
    G.reset()
    n = G.get_n()
    G.dist[start] = 0
    # use heap to optimize the minimum searching
    heap: List[tuple] = [(0, start)]

    path: List[int] = []

    while heap:
        current_dist, u = heapq.heappop(heap)

        # skip if vertex has been visited
        if G.is_visited(u):
            continue

        G.set_visited(u)

        # stop at destomatopm
        if u == destination:
            break

        # check all of u's outgoing edges
        for edge in G.e[u]:
            v = edge.v
            w = edge.w

            # update distance if we find
            # a shorter path is found
            if not G.is_visited(v) and current_dist + w < G.dist[v]:
                G.dist[v] = current_dist + w
                G.set_trace(v, u)
                heapq.heappush(heap, (G.dist[v], v))

    # now if the destination is unreachable
    if G.dist[destination] == 10**9:
        return []

    # reconstruct shortest path by
    # following the traces backwards
    current = destination
    while current != -1:
        path.append(current)
        current = G.trace(current)

    path.reverse()
    return path
