
#Array Queues imp. (4.1)
class ArrayQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Linked list queue imp. (4.2)
class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.is_empty():
            current = self.head
            previous = None
            while current.next:
                previous = current
                current = current.next
            if previous:
                previous.next = None
                if previous == self.head:  # one element
                    self.head = None
            else:
                self.head = None
                self.tail = None
            return current.data
        else:
            raise IndexError("dequeue from an empty queue")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count


