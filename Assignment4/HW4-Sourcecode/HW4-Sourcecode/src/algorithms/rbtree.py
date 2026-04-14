from dataclasses import dataclass
from typing import Optional


@dataclass
class RBNode:
    # stores one node in the red-black tree
    data: int
    x: int
    y: int
    left: Optional["RBNode"] = None
    right: Optional["RBNode"] = None
    parent: Optional["RBNode"] = None
    color: str = "RED"


class RedBlackTree:
    def __init__(self):
        # tree starts empty
        self.root: Optional[RBNode] = None

    def rotate_left(self, root: Optional[RBNode], ptr: Optional[RBNode]) -> None:
        # performs a left rotation around ptr
        if ptr is None or ptr.right is None:
            return

        right_child = ptr.right
        ptr.right = right_child.left

        # if right_child had a left subtree, connect it to ptr
        if right_child.left is not None:
            right_child.left.parent = ptr
        
        # move right_child up into ptr's old position
        right_child.parent = ptr.parent
        if ptr.parent is None:
            self.root = right_child
        elif ptr == ptr.parent.left:
            ptr.parent.left = right_child
        else:
            ptr.parent.right = right_child
        
        # put ptr on the left of right_child
        right_child.left = ptr
        ptr.parent = right_child

    def rotate_right(self, root: Optional[RBNode], ptr: Optional[RBNode]) -> None:
        # performs a right rotation around ptr
        if ptr is None or ptr.left is None:
            return

        left_child = ptr.left
        ptr.left = left_child.right

        # if left_child had a right subtree, connect it to ptr
        if left_child.right is not None:
            left_child.right.parent = ptr
        
        # move left_child up into ptr's old position
        left_child.parent = ptr.parent
        if ptr.parent is None:
            self.root = left_child
        elif ptr == ptr.parent.left:
            ptr.parent.left = left_child
        else:
            ptr.parent.right = left_child
        
        # put ptr on the right of left_child
        left_child.right = ptr
        ptr.parent = left_child

    def fix_violation(self, root: Optional[RBNode], ptr: Optional[RBNode]) -> None:
        # fixes red-black tree violations after insertion
        # the main violation handled here is:
        # a red node cannot have a red parent

        while (ptr is not None and ptr != self.root and ptr.parent is not None and ptr.parent.color == "RED"):
            parent = ptr.parent
            grandparent = parent.parent

            if grandparent is None:
                break

            # case: parent is left child of grandparent
            if parent == grandparent.left:
                uncle = grandparent.right

                # case 1: uncle is red
                # recolor parent and uncle black, grandparent red,
                # then continue fixing upward
                if uncle is not None and uncle.color == "RED":
                    grandparent.color = "RED"
                    parent.color = "BLACK"
                    uncle.color = "BLACK"
                    ptr = grandparent

                else:
                    # case 2: ptr is right child
                    # convert to case 3 by rotating left at parent
                    if ptr == parent.right:
                        self.rotate_left(self.root, parent)
                        ptr = parent
                        parent = ptr.parent

                    # case 3: ptr is left child
                    # rotate right at grandparent and recolor
                    self.rotate_right(self.root, grandparent)
                    parent.color = "BLACK"
                    grandparent.color = "RED"
                    ptr = parent

            # case: parent is right child of grandparent
            else:
                uncle = grandparent.left

                # case 1: uncle is red
                # recolor parent and uncle black, grandparent red,
                # then continue fixing upward
                if uncle is not None and uncle.color == "RED":
                    grandparent.color = "RED"
                    parent.color = "BLACK"
                    uncle.color = "BLACK"
                    ptr = grandparent

                else:
                    # case 2: ptr is left child
                    # convert to case 3 by rotating right at parent
                    if ptr == parent.left:
                        self.rotate_right(self.root, parent)
                        ptr = parent
                        parent = ptr.parent

                    # case 3: ptr is right child
                    # rotate left at grandparent and recolor
                    self.rotate_left(self.root, grandparent)
                    parent.color = "BLACK"
                    grandparent.color = "RED"
                    ptr = parent

        # the root of a red-black tree must always be black
        if self.root is not None:
            self.root.color = "BLACK"

    def insert(self, data: int, x: int, y: int) -> None:
        # creates a new node to insert into the tree
        new_node = RBNode(data, x, y)

        # standard binary search tree insertion
        parent = None
        current = self.root

        while current is not None:
            parent = current
            if new_node.data < current.data:
                current = current.left
            elif new_node.data > current.data:
                current = current.right
            else:
                # do not insert duplicate values
                return

        # link the new node to its parent
        new_node.parent = parent

        if parent is None:
            # tree was empty, so new node becomes root
            self.root = new_node
        elif new_node.data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        # if inserted node is root, it must be black
        if new_node.parent is None:
            new_node.color = "BLACK"
            return

        # if there is no grandparent, there cannot be a violation yet
        if new_node.parent.parent is None:
            return

        # fix any red-black property violations caused by insertion
        self.fix_violation(self.root, new_node)

    def search(self, data: int) -> Optional[RBNode]:
        # searches for a node with the given data value
        temp = self.root

        while temp is not None:
            if data == temp.data:
                return temp
            if data < temp.data:
                temp = temp.left
            else:
                temp = temp.right

        # return none if value is not found
        return None