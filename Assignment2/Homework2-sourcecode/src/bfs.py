from graph import Graph
from queue import Queue

# Breadth-First Search (BFS)
# Uses a queue (FIFO) to explore the graph level by level.
# Ensures the shortest path (in number of edges) is found in an unweighted graph.
# visited prevents revisiting nodes and infinite cycles.
# g.set_trace(v, u) records the parent of each node for path reconstruction.

def bfs(g: Graph, start: int, destination: int) -> None:
    queue: Queue[int] = Queue()
    g.reset()

    # add start to the queue so it gets explored later
    queue.push(start)
    # create and add start to the visited state
    g.set_visited(start)

    # while queue is still available
    while not queue.empty():
        u = queue.pop()
        # dequeue to move onto the next node to explore

        # if this node is the goal lets call it quits
        if u == destination:
            return
        
        # gets the number of neighbors to node u
        number_of_adjacency_nodes = g.e[u].size()
        p = g.e[u].get_root()
        # set p to be the head of the adjacency list for node u

        # iterate through neighbors of u
        for _ in range(number_of_adjacency_nodes):
            v = p.value
            
            # now if this neighbor has not been visited add it
            if not g.is_visited(v):
                g.set_visited(v)
                # add tracr from node to node on graph by traversing the edges between v and u
                g.set_trace(v, u)
                # add this to the list of nodes to explore
                queue.push(v)
                
            p = p.next
