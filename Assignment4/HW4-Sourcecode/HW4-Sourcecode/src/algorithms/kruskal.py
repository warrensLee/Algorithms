from typing import List

from data_structures.disjoint_set import DisjointSet
from graph import Edge, Graph

# helper function to merge two sorted halves of edges
def merge_edges(edges: List[Edge], l: int, m: int, r: int) -> None:
    # create left and right subarrays
    left = edges[l:m + 1]
    right = edges[m + 1:r + 1]

    i = 0
    j = 0
    k = l

    # merge based on edge weight
    while i < len(left) and j < len(right):
        if left[i].w <= right[j].w:
            edges[k] = left[i]
            i += 1
        else:
            edges[k] = right[j]
            j += 1
        k += 1

    # copy remaining elements from left if any
    while i < len(left):
        edges[k] = left[i]
        i += 1
        k += 1

    # copy remaining elements from right if any
    while j < len(right):
        edges[k] = right[j]
        j += 1
        k += 1


# helper function to perform merge sort on edges
def merge_sort_edges(edges: List[Edge], l: int, r: int) -> None:
    # recursively divide the list into halves
    if l < r:
        m = (l + r) // 2
        merge_sort_edges(edges, l, m)
        merge_sort_edges(edges, m + 1, r)
        merge_edges(edges, l, m, r)


def construct_mst_kruskal(G: Graph) -> List[Edge]:
    edges = G.export_edges()  # Graph's edges
    # DisjointSet djs(G.n);
    # Use Disjoint Set to check whether two vertices are on the same set
    # Usage: Check djs.is_on_same_set(u, v); Check is u and v is on the same set or not
    # djs.join(u, v); Join sets of u and v into the same set
    mst: List[Edge] = []
    djs = DisjointSet(G.get_n())

    n = G.get_n()

    # sort edges in weight ascending order using merge sort,
    # then we will handle each edge in that order
    if len(edges) > 1:
        merge_sort_edges(edges, 0, len(edges) - 1)

    for edge in edges:
        u, v = edge.u, edge.v

        # if u & v are not connected, add an edge
        if not djs.is_on_same_set(u, v):
            mst.append(edge)
            djs.join(u, v)

        # when MST has n - 1 edges
        if len(mst) == n - 1:
            break

    # after the loop, check for
    # a disconnected graph to ensure
    # that MST can include all vertices
    if len(mst) != n - 1:
        return []

    return mst