from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class QueueNode(Generic[T]):
    value: T
    next: Optional["QueueNode[T]"] = None
    prev: Optional["QueueNode[T]"] = None


class Queue(Generic[T]):
    def __init__(self) -> None:
        self._head: Optional[QueueNode[T]] = None
        self._tail: Optional[QueueNode[T]] = None

    def empty(self) -> bool:
        return self._head is None and self._tail is None

    def pop(self) -> T:
        if self._head is None:
            raise IndexError("pop from empty queue")
        value = self._head.value
        p = self._head
        if p.next is None:
            self._head = self._tail = None
        else:
            self._head = p.next
            self._head.prev = None
        return value

    def push(self, value: T) -> None:
        node = QueueNode(value=value, next=None, prev=None)
        if self._tail is None:
            self._head = self._tail = node
        else:
            self._tail.next = node
            node.prev = self._tail
            self._tail = node
