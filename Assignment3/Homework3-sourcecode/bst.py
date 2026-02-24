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

    def clear(self, node: Optional[BSTNode]) -> None:
        # YOUR CODE HERE
        pass

    def _find(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def _findMaximum(self, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def _findMinimum(self, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def _insert(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

    def _remove(self, key: T, node: Optional[BSTNode]) -> Optional[BSTNode]:
        # YOUR CODE HERE
        return None  # Placeholder

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
