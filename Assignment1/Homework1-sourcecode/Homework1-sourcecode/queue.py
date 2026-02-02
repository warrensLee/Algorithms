class QueueNode:
    def __init__(self, value: int = None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

# first in first out like a line at chic-fil-a


class Queue:
    def __init__(self):
        self.head = None        # where u pop
        self.tail = None        # where u push

    def empty(self) -> bool:
        # YOUR CODE HERE
        # if the beginning and end both == None, then this queue is empty!
        if self.head is None and self.tail is None:
            return True
        return False
        # END OF YOUR CODE HERE

    def pop(self) -> int:
        if self.empty():
            raise IndexError("Queue is empty")
        # YOUR CODE HERE
        # if there is only one element in queue
        val = self.head.value
        if self.head.next == None:
            self.head = None
            self.tail = None
            return val
        # if there is more than one element in queue
        else:
            # increment the head (like moving the whole list over)
            self.head = self.head.next
            self.head.prev = None           # ensure previous head value is removed properly
            return val
        # END OF YOUR CODE HERE

    def push(self, value: int):
        node = QueueNode(value, None, None)
        # YOUR CODE HERE
        # if queue is empty (add it as head and tail):
        if self.empty():
            self.head, self.tail = node, node
        # if queue is not empty (add it as tail):
        else:
            node.prev = self.tail       # make the node before the new node the previous tail
            self.tail.next = node       # set the node after current tail to the new node
            self.tail = self.tail.next  # current tail must become new node
            # self.tail.next = None       # ensure this list ends with nothing (redudant due to node = QueueNode(value, None, None))
        # END OF YOUR CODE HERE
