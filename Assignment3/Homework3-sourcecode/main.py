import sys
from bst import BST
from avl import AVL
from graph import Graph
from bfs import bfs

################################################################################
# This Section is for the Grader. Do not modify this section.
# Global constant filename. For Grading purpose. Don't modify this variable.
testcases = "../HW3-testcase/testcases.txt"
map_info_testcases = "../HW3-testcase/map_info.txt"


# Function for Grading purpose. Don't modify this function.
def searchOnCampus(start="BELL", destination="HAPG", map_file="assets/map_info.txt"):
    with open(map_file) as reader:
        n, m = map(int, reader.readline().split())
        name2index = {}
        index2name = {}
        xs = []
        ys = []
        for _ in range(n):
            parts = reader.readline().split()
            index, name = int(parts[0]), parts[1]
            x, y = int(parts[2]), int(parts[3])
            xs.append(x)
            ys.append(y)
            name2index[name] = index
            index2name[index] = name

        G = Graph(n)
        for _ in range(m):
            u, v = map(int, reader.readline().split())
            dx = xs[u] - xs[v]
            dy = ys[u] - ys[v]
            w = dx * dx + dy * dy
            G.insertEdge(u, v, w)

    path = G.search(name2index[start], name2index[destination], bfs)

    path_string = "Shortest path from " + start + " to " + destination + ": " + start
    for i in range(1, len(path)):
        path_string += " -> " + index2name[path[i]]

    print(path_string)
    print("Total Distance: " + str(G.distance(name2index[destination])))

    return path_string


def testCases():
    try:
        input_file = open(testcases)
    except OSError:
        return

    score = 0
    try:
        line = input_file.readline()
        test_cases = int(line.strip())
    except (ValueError, TypeError):
        print("Error: Invalid file format (no test case count).", file=sys.stderr)
        return
    input_file.readline()

    for i in range(test_cases):
        line = input_file.readline()
        parts = line.split()
        if len(parts) < 2:
            print("Warning: Expected more lines than found in file.", file=sys.stderr)
            break
        start, destination = parts[0], parts[1]
        expected_path = input_file.readline().strip()

        print("\n-------------------------------")
        result = searchOnCampus(start, destination, map_info_testcases)

        print("Test Case " + str(i + 1) + ":")
        print(" Expected: " + expected_path)
        if result == expected_path:
            print("The strings are equal!")
            score += 5
        else:
            print("The strings are different.")
        print("-------------------------------")

    print("Total Score: " + str(score) + " / " + str(test_cases * 5))


# End of Grader section
################################################################################


def isAVLValid(node, min_key, max_key):
    if node is None:
        return True

    # 1. Check BST Property
    if (min_key is not None and node.key < min_key) or (max_key is not None and node.key > max_key):
        print("[Error] BST property violated at key: " + str(node.key))
        return False

    # 2. Check Height consistency and Balance Factor
    left_h = node.left.height if node.left else -1
    right_h = node.right.height if node.right else -1

    if node.height != max(left_h, right_h) + 1:
        print("[Error] Height property mismatch at node " + str(node.key))
        return False

    if abs(left_h - right_h) > 1:
        print("[Error] Unbalanced node found at key: " + str(node.key))
        return False

    return isAVLValid(node.left, min_key, node.key) and isAVLValid(node.right, node.key, max_key)


def testBST():
    bst = BST()
    for i in range(10):
        print("Insert " + str(i) + " into BST")
        bst.insert(i)

        print("Find " + str(i) + ". ")
        if bst.find(i) is not None and bst.find(i).key == i:
            print("Found " + str(i) + " in BST")
        else:
            return False

        print("Find " + str(i + 1) + ". ")
        if bst.find(i + 1) is None:
            print("Not found " + str(i + 1) + " in BST")
        else:
            return False

        print()

    print("Maximum value in BST: ")
    if bst.findMaximum() is None or bst.findMaximum().key != 9:
        return False
    else:
        print(str(bst.findMaximum().key) + "\n")

    for i in range(9):
        print("Remove " + str(i) + " out of BST")
        bst.remove(i)

        print("Find " + str(i) + ". ")
        if bst.find(i) is None:
            print("Not found " + str(i) + " in BST")
        else:
            return False

        print("Find " + str(i + 1) + ". ")
        if bst.find(i + 1) is not None and bst.find(i + 1).key == i + 1:
            print("Found " + str(i + 1) + " in BST")
        else:
            return False
        print()

    return True


def testAVL():
    avl = AVL()
    print("--- Starting AVL Unit Test ---")

    for i in range(10):
        print("Insert " + str(i) + " into AVL")
        avl.insert(i)

        if avl.getRoot() is not None:
            print("Current Tree Height (at root): " + str(avl.getRoot().height))

        print("Find " + str(i) + ". ")
        if avl.find(i) is not None and avl.find(i).key == i:
            print("Found " + str(i) + " in AVL")
        else:
            print("Failed to find " + str(i))
            return False

        if not isAVLValid(avl.getRoot(), None, None):
            print("Structural integrity check failed!")
            return False
        print()

    print("Maximum value in AVL: ")
    if avl.findMaximum() is None or avl.findMaximum().key != 9:
        print("Error in findMaximum")
        return False
    print(str(avl.findMaximum().key) + "\n")

    for i in range(9):
        print("Remove " + str(i) + " out of AVL")
        avl.remove(i)

        print("Find " + str(i) + ". ")
        if avl.find(i) is None:
            print("Not found " + str(i) + " in AVL")
        else:
            print("Error: " + str(i) + " still found in AVL")
            return False

        print("Find " + str(i + 1) + ". ")
        if avl.find(i + 1) is not None and avl.find(i + 1).key == i + 1:
            print("Found " + str(i + 1) + " in AVL")
        else:
            return False

        if avl.getRoot() is not None:
            print("Tree height after removal: " + str(avl.getRoot().height))

        if not isAVLValid(avl.getRoot(), None, None):
            print("Structural integrity check failed after removal!")
            return False
        print()

    return True


if __name__ == "__main__":
    print("Perform unit test on your BST implementation")
    if testBST():
        print("Your BST implementation is correct")
    else:
        print("Your BST implementation is incorrect")
        sys.exit(-1)

    print("Perform unit test on your AVL implementation")

    if testAVL():
        print("Your AVL implementation is correct")
    else:
        print("Your AVL implementation is incorrect")
        sys.exit(-1)

    print("\n\n")

    searchOnCampus("JBHT", "HAPG")

    print("\n")

    # THE FOLLOWING FUNCTION IS FOR GRADING PURPOSE. DON'T MODIFY THIS FUNCTION.
    testCases()
