import sys
from pathlib import Path

from graph import Graph
from linked_list import LinkedList
from queue import Queue


def test_linked_list():
    linked_list = LinkedList()
    linked_list.insert(10)
    linked_list.insert(100)

    if linked_list.find(10):
        print("10 is in the linked list")
    else:
        return False

    if linked_list.find(20):
        return False
    else:
        print("20 is not in the linked list")

    if linked_list.find(100):
        print("100 is in the linked list")
    else:
        return False

    if linked_list.size() == 2:
        print("The linked list has 2 nodes")
    else:
        return False

    linked_list.remove(100)

    if linked_list.find(100):
        return False
    else:
        print("100 is not in the linked list")

    if linked_list.size() == 1:
        print("The linked list has 1 node")
    else:
        return False

    return True


def test_queue():
    queue = Queue()
    queue.push(0)
    if queue.empty():
        return False
    else:
        print("Queue is not empty")

    if queue.pop() == 0:
        print("Remove first node in queue successfully")
    else:
        return False

    if queue.empty():
        print("Queue is empty")
    else:
        return False

    return True


def test_graph():
    graph = Graph(6)
    graph.insert_edge(0, 1)
    graph.insert_edge(1, 2)
    graph.insert_edge(1, 3)
    graph.insert_edge(2, 4)
    graph.insert_edge(4, 3)
    graph.insert_edge(4, 5)

    print("Path from 0 to 5: ", end="")
    path = graph.search(0, 5)
    for node in path:
        print(f"{node} ", end="")
    print()
    return True


def search_on_campus(start="BELL", destination="HAPG"):
    assets_dir = Path(__file__).resolve().parent / "assets"
    with (assets_dir / "map_info.txt").open() as reader:
        tokens = reader.read().split()

    it = iter(tokens)
    n = int(next(it))
    m = int(next(it))

    name2index = {}
    index2name = {}
    xs = []
    ys = []
    for _ in range(n):
        index = int(next(it))
        name = next(it)
        x = int(next(it))
        y = int(next(it))
        xs.append(x)
        ys.append(y)
        name2index[name] = index
        index2name[index] = name

    graph = Graph(n)

    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        graph.insert_edge(u, v)

    path = graph.search(name2index[start], name2index[destination])

    print(f"Path from {start} to  detination: {start}", end="")
    for i in range(1, len(path)):
        print(f" -> {index2name[path[i]]}", end="")
    print()

    try:
        import cv2
    except ImportError:
        print("You have to use OpenCV to visualize your map road")
        return

    image = cv2.imread(str(assets_dir / "map.png"))
    for i in range(n):
        cv2.circle(image, (xs[i], ys[i]), 10, (255, 0, 0), -1)
        cv2.putText(
            image,
            index2name[i],
            (xs[i], ys[i] - 10),
            cv2.FONT_HERSHEY_DUPLEX,
            0.7,
            (255, 0, 0),
            1,
        )

    for i in range(len(path)):
        if i > 0:
            cv2.line(
                image,
                (xs[path[i]], ys[path[i]]),
                (xs[path[i - 1]], ys[path[i - 1]]),
                (255, 0, 0),
                4,
            )
    cv2.imshow(f"Path from {start} to {destination}", image)
    cv2.waitKey(0)


if __name__ == "__main__":
    if test_linked_list():
        print("Your linked list implementation is correct")
    else:
        print("Your linked list implementation is incorrect")
        sys.exit(1)

    print("\n\n")

    if test_queue():
        print("Your queue implementation is correct")
    else:
        print("Your queue implementation is incorrect")
        sys.exit(1)

    print("\n\n")

    if test_graph():
        print("Your linked list and queue implementation is correct")
    else:
        print("Your linked list and queue implementation is incorrect")
        sys.exit(1)

    print("\n\n")

    search_on_campus("BELL", "HAPG")

    print("\n")
