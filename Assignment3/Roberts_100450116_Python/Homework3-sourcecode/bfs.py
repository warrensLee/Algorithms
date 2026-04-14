from typing import TYPE_CHECKING
from avl import AVL
from bst import BSTNode

if TYPE_CHECKING:
    from graph import Graph


def bfs(G: 'Graph', start: int, destination: int) -> None:
    # We use AVL for O(log n) efficiency to keep the priority queue balanced
    priority_queue = AVL()

    G.reset()
    G.dist[start] = 0

    # Insert initial node (distance, index)
    priority_queue.insert((G.distance(start), start))
    G.setTrace(start, -1)

    while True:
        # Get the node with the SHORTEST distance
        min_node = priority_queue.findMinimum()

        if min_node is None:
            break

        current = min_node.key
        priority_queue.remove(current)

        # Optimization: If we found a better way to 'u' already, skip this stale entry
        if current[0] > G.distance(current[1]):
            continue

        u = current[1]
        dist = current[0]

        G.setVisited(u)

        if u == destination:
            break

        number_of_adjacency_nodes = G.e[u].size()
        p = G.e[u].getRoot()
        for _ in range(number_of_adjacency_nodes):
            v = p.value[0]
            weight = p.value[1]

            if G.isVisited(v):
                p = p.next
                continue

            # Relaxation Step
            if dist + weight < G.distance(v):
                G.dist[v] = dist + weight
                priority_queue.insert((G.distance(v), v))
                G.setTrace(v, u)

            p = p.next
