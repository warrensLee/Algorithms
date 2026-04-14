from typing import Optional, TypeVar

T = TypeVar('T')


class LinkedListNode:
    def __init__(self, value: T = None, next_node: Optional['LinkedListNode'] = None, prev: Optional['LinkedListNode'] = None):
        self.value = value
        self.next = next_node
        self.prev = prev

    def __del__(self):
        self.next = None


class LinkedList:
    def __init__(self):
        self.root: Optional[LinkedListNode] = None

    def insert(self, value: T) -> Optional[LinkedListNode]:
        p = self.find(value)
        if p is not None:
            return p
        p = LinkedListNode(value, None)
        if self.root is None:
            self.root = p
        else:
            p.next = self.root
            self.root = p
        return p

    def find(self, value: T) -> Optional[LinkedListNode]:
        p = self.root
        while p is not None and p.value != value:
            p = p.next
        return p

    def getRoot(self) -> Optional[LinkedListNode]:
        return self.root

    def remove(self, value: T) -> Optional[LinkedListNode]:
        p = self.root
        q = None
        while p is not None:
            if p.value == value:
                if q is None:
                    self.root = p.next
                else:
                    q.next = p.next
                break
            q = p
            p = p.next
        return self.root

    def size(self) -> int:
        cnt = 0
        p = self.root
        while p is not None:
            cnt += 1
            p = p.next
        return cnt
