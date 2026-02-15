from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar("T")


@dataclass
class StackNode(Generic[T]):
    value: T
    next: Optional["StackNode[T]"] = None


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._head: Optional[StackNode[T]] = None

    def empty(self) -> bool:
        return self._head is None

    def pop(self) -> T:
        if self._head is None:
            raise IndexError("pop from empty stack")
        value = self._head.value
        self._head = self._head.next
        return value

    def push(self, value: T) -> None:
        self._head = StackNode(value=value, next=self._head)
