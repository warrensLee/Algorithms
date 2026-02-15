from dataclasses import dataclass
from typing import Generic, Optional, TypeVar, Iterator

T = TypeVar("T")


@dataclass
class LinkedListNode(Generic[T]):
    value: T
    next: Optional["LinkedListNode[T]"] = None
    prev: Optional["LinkedListNode[T]"] = None


class LinkedList(Generic[T]):
    def __init__(self) -> None:
        self._root: Optional[LinkedListNode[T]] = None

    def insert(self, value: T) -> LinkedListNode[T]:
        """Insert value at the head if not present; return existing node if present."""
        existing = self.find(value)
        if existing is not None:
            return existing
        node = LinkedListNode(value=value, next=self._root, prev=None)
        if self._root is not None:
            self._root.prev = node
        self._root = node
        return node

    def find(self, value: T) -> Optional[LinkedListNode[T]]:
        p = self._root
        while p is not None and p.value != value:
            p = p.next
        return p

    def remove(self, value: T) -> Optional[LinkedListNode[T]]:
        p = self._root
        q: Optional[LinkedListNode[T]] = None
        while p is not None:
            if p.value == value:
                # remove p
                if q is None:
                    self._root = p.next
                    if self._root is not None:
                        self._root.prev = None
                else:
                    q.next = p.next
                    if q.next is not None:
                        q.next.prev = q
                break
            q = p
            p = p.next
        return self._root

    def size(self) -> int:
        cnt = 0
        p = self._root
        while p is not None:
            cnt += 1
            p = p.next
        return cnt

    def get_root(self) -> Optional[LinkedListNode[T]]:
        return self._root

    def __iter__(self) -> Iterator[T]:
        p = self._root
        while p is not None:
            yield p.value
            p = p.next
