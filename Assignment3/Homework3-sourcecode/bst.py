from typing import Optional, TypeVar

T = TypeVar('T')


class BSTNode:
    def __init__(self, key: T = None, height: int = 0, left: Optional['BSTNode'] = None, right: Optional['BSTNode'] = None):
        if key is not None:
            self.key = key
        self.height = height
        self.left = left if left is not None else None
        self.right = right if right is not None else None

    def __del__(self):
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root: Optional[BSTNode] = None

    def __del__(self):
        self.clear(self.root)
        self.root = None


    # def clear(self, node: Optional[BSTNode]): Release (deallocate) the memory of all nodes in the
    # subtree whose root is given by the parameter node. In Python, this can be done by assigning each
    # node reference to None.
    def clear(self, node: Optional[BSTNode]) -> None:
        # base case to end recursion at the end of the tree
        if node is None:
            return

        # recursive clearing
        self.clear(node.left)
        self.clear(node.right)
        
        # remove values
        node.left = None
        node.right = None


    # def find(self, key: T, node: Optional[BSTNode]): Find the given key in the subtree whose
    # root is the parameter node. If the key exists in the subtree, return a pointer to the node containing
    # the key; otherwise, return the NULL pointer.
    def _find(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # get the root
        current = self.root

        # now while this node is not null
        while current is not None:
            # if we found the key
            if key == current.key:
                return current
            # key < this key move to left
            elif key < current.key:
                current = current.left
            # key > this key move to right
            else: 
                current = current.right

        return None  # Placeholder


    # def findMaximum(self, node: Optional[BSTNode]): Find the maximum key in the subtree whose
    # root is the parameter node. Return a pointer to the node containing the maximum key. If the subtree
    # is empty, return the NULL pointer. The findMinimum function is similar.
    def _findMaximum(self, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # if node is null stop
        if node is None:
            return None
        
        # for iteration
        current = node

        # while right node is not null
        # iterratie the current node->right
        while current.right is not None:
            current = current.right

        return current  


    def _findMinimum(self, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # if node is null stop
        if node is None:
            return None
        
        # for iteration
        current = node

        # while left node is not null
        # iterratie the current node->left
        while current.left is not None:
            current = current.left

        return current  


    # def insert(self, key: T, node: Optional[BSTNode]): Insert the given key into the subtree
    # whose root is the parameter node. Return the root pointer of the subtree after insertion. If the key
    # already exists, return the root unchanged (duplicate keys are not inserted).
    def _insert(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # escape the recursion
        # create new node at first empty spot
        # (after correct traversal)
        if node is None:
            return BSTNode(key)

        # if we have found a node with the same key
        # that we are trying to insert
        if key == node.key:
            return node
        
        # now to recursively insert
        if key < node.key:
            node.left = self._insert(key, node.left)
        else:
            node.right = self._insert(key, node.right)

        return node
    

    # def remove(self, key: T, node: Optional[BSTNode]): Remove the given key from the sub-
    # tree whose root is the parameter node. Return the root pointer of the subtree after deletion.
    def _remove(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # if we have found a node with the same key
        # that we are trying to insert
        if node is None:
            return node
        
        # now to recursively search
        if key < node.key:
            node.left = self._remove(key, node.left)
        elif key > node.key:
            node.right = self._remove(key, node.right)
            
        else:
            # node with 0 or 1 children:

            # no left child
            if node.left is None:
                return node.right
            # no right child
            if node.right is None:
                return node.left
            
            # node with 2 children
            temp = self._findMinimum(node.right)
            node.key = temp.key
            node.right = self._remove(temp.key, node.right)

        return node

    def find(self, key: T) -> Optional[BSTNode]:
        return self._find(key, self.root)

    def findMaximum(self) -> Optional[BSTNode]:
        return self._findMaximum(self.root)

    def findMinimum(self) -> Optional[BSTNode]:
        return self._findMinimum(self.root)

    def insert(self, key: T) -> Optional[BSTNode]:
        self.root = self._insert(key, self.root)
        return self.root

    def remove(self, key: T) -> Optional[BSTNode]:
        self.root = self._remove(key, self.root)
        return self.root

    def getRoot(self) -> Optional[BSTNode]:
        return self.root
