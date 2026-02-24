from typing import Optional, TypeVar
from bst import BST, BSTNode

T = TypeVar('T')


class AVL(BST):
    def getHeight(self, node: Optional[BSTNode]) -> int:
        return -1 if node is None else node.height

    def getBalance(self, node: Optional[BSTNode]) -> int:
        return 0 if node is None else self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, y: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def rotateLeft(self, x: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def _insert(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def _remove(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def insert(self, key: T) -> Optional[BSTNode]:
        self.root = self._insert(key, self.root)
        return self.root

    def remove(self, key: T) -> Optional[BSTNode]:
        self.root = self._remove(key, self.root)
        return self.root
