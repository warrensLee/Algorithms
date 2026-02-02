class LinkedListNode:
    def __init__(self, value: int = None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> LinkedListNode:
        # YOUR CODE HERE
        exists = self.find(value)  # check if value already exists
        if exists is None:
            new_node = LinkedListNode(value)
            new_node.next = self.root
            self.root = new_node
            return new_node
        return exists
        # END OF YOUR CODE

    def find(self, value: int) -> LinkedListNode:
        # YOUR CODE HERE
        p = self.root
        while p:
            if p.value == value:
                return p
            p = p.next
        return None
        # END OF YOUR CODE

    def remove(self, value: int) -> LinkedListNode:
        # YOUR CODE HERE
        curr = self.root
        prev = None

        while curr:
            if curr.value == value:         # if this value is to be removed
                if prev is None:
                    self.root = curr.next
                else:
                    prev.next = curr.next
                break
            prev = curr
            curr = curr.next

        return self.root
        # END OF YOUR CODE

    def size(self) -> int:
        # YOUR CODE HERE
        count = 0
        p = self.root
        while p:  # while p is valid
            count += 1
            p = p.next
        return count
        # END OF YOUR CODE

    def __iter__(self):
        p = self.root
        while p:
            yield p.value
            p = p.next
