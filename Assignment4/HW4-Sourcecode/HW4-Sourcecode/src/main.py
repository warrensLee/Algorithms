import math
import random
from typing import Dict, List

from algorithms.dijkstra import search_shortest_path
from algorithms.kruskal import construct_mst_kruskal
from algorithms.prim import construct_mst_prim
from algorithms.rbtree import RedBlackTree
from algorithms.topologicalsort import topological_sort
from graph import Edge, Graph
from sort.hsort import heap_sort
from sort.msort import msort

PRIM = True
KRUSKAL = True
DIJKSTRA = True
INTEGRATED = True


def test_sort(sort_kind: int) -> bool:
    data: List[int] = [random.randint(0, 49) for _ in range(20)]
    print("Original array:", *data)

    if sort_kind == 0:
        heap_sort(data)
    elif sort_kind == 1:
        msort(data, 0, len(data))
    else:
        print("Invalid sort type!")
        return False

    print("Sorted array:", *data)
    return data == sorted(data)


def test_mst(algo: int) -> bool:
    G = Graph(6)
    G.insert_edge(0, 1, 1)
    G.insert_edge(1, 2, 2)
    G.insert_edge(1, 3, 3)
    G.insert_edge(2, 4, 4)
    G.insert_edge(4, 3, 5)
    G.insert_edge(4, 5, 6)

    tree: List[Edge] = []
    if algo == 1:
        tree = construct_mst_prim(G)
    elif algo == 2:
        tree = construct_mst_kruskal(G)

    total_cost = sum(edge.w for edge in tree)
    print("Total Cost of Minimum Spanning Tree:", total_cost)
    return True

def mst_on_campus(algo: int) -> None:
    with open("assets/map_info.txt", "r", encoding="utf-8") as reader:
        n, m = map(int, reader.readline().split())
        name2index: Dict[str, int] = {}
        index2name: Dict[int, str] = {}
        xs: List[int] = []
        ys: List[int] = []

        for _ in range(n):
            index, name, x, y = reader.readline().split()
            index_int = int(index)
            x_int = int(x)
            y_int = int(y)
            xs.append(x_int)
            ys.append(y_int)
            name2index[name] = index_int
            index2name[index_int] = name

        G = Graph(n)
        for _ in range(m):
            u, v = map(int, reader.readline().split())
            dx = xs[u] - xs[v]
            dy = ys[u] - ys[v]
            w = int(math.sqrt(dx * dx + dy * dy))
            G.insert_edge(u, v, w)

    tree: List[Edge] = []
    if algo == 1:
        tree = construct_mst_prim(G)
    elif algo == 2:
        tree = construct_mst_kruskal(G)

    total_cost = sum(edge.w for edge in tree)
    print("Total Cost of Minimum Spanning Tree:", total_cost)

def test_shortest_path() -> bool:
    G = Graph(6)
    G.insert_edge(0, 1, 1)
    G.insert_edge(1, 2, 2)
    G.insert_edge(1, 3, 3)
    G.insert_edge(2, 4, 4)
    G.insert_edge(4, 3, 5)
    G.insert_edge(4, 5, 6)

    start_node = 0
    dest_node = 5
    path = search_shortest_path(G, start_node, dest_node)

    # HANDLE FALSE: Check if the path is empty or unreachable
    if not path:
        print(f"Path from {start_node} to {dest_node}: NO PATH FOUND")
        return False

    # Additional check: If the path doesn't end at the destination, it's invalid
    if path[-1] != dest_node:
        print("Pathfinding error: Destination not reached.")
        return False

    print(f"Path from {start_node} to {dest_node}:", " -> ".join(map(str, path)))
    return True

def search_on_campus(start: str = "BELL", destination: str = "HAPG") -> None:
    with open("assets/map_info.txt", "r", encoding="utf-8") as reader:
        n, m = map(int, reader.readline().split())
        name2index: Dict[str, int] = {}
        index2name: Dict[int, str] = {}
        xs: List[int] = []
        ys: List[int] = []

        for _ in range(n):
            index, name, x, y = reader.readline().split()
            index_int = int(index)
            x_int = int(x)
            y_int = int(y)
            xs.append(x_int)
            ys.append(y_int)
            name2index[name] = index_int
            index2name[index_int] = name

        G = Graph(n)
        for _ in range(m):
            u, v = map(int, reader.readline().split())
            dx = xs[u] - xs[v]
            dy = ys[u] - ys[v]
            w = int(math.sqrt(dx * dx + dy * dy))
            G.insert_edge(u, v, w)

    path = search_shortest_path(G, name2index[start], name2index[destination])
    print(
        f"Path from {start} to {destination}:",
        " -> ".join(index2name[node] for node in path),
    )


def combined_algorithm_demo() -> None:
    print("\n==========================================================")
    print("--- STARTING INTEGRATED ALGORITHM STACK DEMO ---")
    print("==========================================================")

    try:
        building_db = RedBlackTree()
        building_db.insert(0, 100, 100)
        building_db.insert(1, 200, 300)
        building_db.insert(2, 400, 150)
        print("[Step 1] RB-Tree: Coordinates stored for Buildings 0, 1, and 2.")

        b0 = building_db.search(0)
        b1 = building_db.search(1)
        b2 = building_db.search(2)

        # HANDLE FALSE: Validation check for Tree Retrieval
        if not b0 or not b1 or not b2:
            raise RuntimeError(
                "RB-Tree Error: One or more buildings could not be retrieved."
            )

        print(f" -> Found Building {b0.data} at ({b0.x}, {b0.y})")
        print(f" -> Found Building {b1.data} at ({b1.x}, {b1.y})")
        print(f" -> Found Building {b2.data} at ({b2.x}, {b2.y})")

        G = Graph(3)
        d01 = int(math.sqrt((b1.x - b0.x) ** 2 + (b1.y - b0.y) ** 2))
        d12 = int(math.sqrt((b2.x - b1.x) ** 2 + (b2.y - b1.y) ** 2))
        d02 = int(math.sqrt((b2.x - b0.x) ** 2 + (b2.y - b0.y) ** 2))

        G.insert_edge(0, 1, d01)
        G.insert_edge(1, 2, d12)
        G.insert_edge(0, 2, d02)

        print("\n[Step 2] Graph: Edges created with Euclidean weights:")
        print(" -> Edge (0,1) weight:", d01)
        print(" -> Edge (1,2) weight:", d12)
        print(" -> Edge (0,2) weight:", d02)

        print("\n[Step 3] Kruskal: Constructing Minimum Spanning Tree...")
        mst = construct_mst_kruskal(G)
        if not mst:
            raise RuntimeError(
                "Kruskal Error: MST could not be formed (Graph may be disconnected)."
            )
        mst_cost = 0
        for edge in mst:
            print(f" -> Added Edge ({edge.u},{edge.v}) w:{edge.w}")
            mst_cost += edge.w
        print("Total MST Cost:", mst_cost)

        print("\n[Step 4] Dijkstra: Calculating shortest path from 0 to 2...")
        path = search_shortest_path(G, 0, 2)

        # HANDLE FALSE: Check if destination was reached
        if not path or path[-1] != 2:
            raise RuntimeError("Dijkstra Error: No path found between specified nodes.")

        print(" -> Shortest Path:", " -> ".join(map(str, path)))

        congestion = [85, 12, 44, 98, 30]
        print("\n[Step 5] HeapSort: Sorting traffic congestion scores...")
        print(" -> Original: 85 12 44 98 30")
        heap_sort(congestion)
        print(" -> Sorted:  ", *congestion)

    except Exception as exc:
        print(f"\n[ERROR]: {exc}")

    print("\n==========================================================")
    print("--- INTEGRATED DEMO COMPLETE ---")
    print("==========================================================")


if __name__ == "__main__":
    print("Perform unit test on heap sort")
    if test_sort(0):
        print("Your sorting implementation is correct\n")
    else:
        print("Your sorting implementation is incorrect\n")
        raise SystemExit(1)

    print("Perform unit test on Merge sort")
    if test_sort(1):
        print("Your sorting implementation is correct\n")
    else:
        print("Your sorting implementation is incorrect\n")
        raise SystemExit(1)

    print("\nPerform unit test on Topological sort")
    g = Graph(6)
    g.insert_edge(5, 0, 1, True)
    g.insert_edge(5, 2, 1, True)
    g.insert_edge(4, 0, 1, True)
    g.insert_edge(4, 1, 1, True)
    g.insert_edge(2, 3, 1, True)
    g.insert_edge(3, 1, 1, True)

    result = topological_sort(g)
    print("Topological Sort:", *result)
    if len(result) == 6:
        print("Topological Sort implementation is correct.")
    else:
        print("Topological Sort implementation is incorrect. Not all nodes processed.")
        raise SystemExit(1)

    if PRIM:
        print("Perform unit test of the Prim's algorithm")
        test_mst(1)
        print()
        mst_on_campus(1)

    if KRUSKAL:
        print("\nPerform unit test of the Kruskal's algorithm")
        test_mst(2)
        print()
        mst_on_campus(2)

    if DIJKSTRA:
        print("\nPerform unit test of the Dijkstra algorithm")
        test_shortest_path()
        print()
        search_on_campus("SAEF", "GRAD")

    if INTEGRATED:
        print("\nPerform unit test of the Red-Black Tree")
        combined_algorithm_demo()
