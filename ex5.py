# Q1

class CircularQueueArray:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.front = self.size = 0
        self.rear = capacity - 1
        self.capacity = capacity

    def isFull(self):
        return self.size == self.capacity

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        if self.isFull():
            print("enqueue None")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"enqueue {item}")

    def dequeue(self):
        if self.isEmpty():
            print("dequeue None")
            return None
        front_item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"dequeue {front_item}")
        return front_item

    def peek(self):
        if self.isEmpty():
            print("peek None")
            return None
        print(f"peek {self.queue[self.front]}")
        return self.queue[self.front]

# Q2
    
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CircularQueueLinkedList:
    def __init__(self):
        self.front = self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front
        print(f"enqueue {item}")

    def dequeue(self):
        if self.front is None:
            print("dequeue None")
            return None
        if self.front == self.rear:  # Queue has only one node
            temp = self.front
            self.front = self.rear = None
        else:
            temp = self.front
            self.front = self.front.next
            self.rear.next = self.front
        print(f"dequeue {temp.value}")
        return temp.value

    def peek(self):
        if self.front is None:
            print("peek None")
            return None
        print(f"peek {self.front.value}")
        return self.front.value

# Q3
    
# Initialize the circular queue with a fixed size of 5 for the array implementation
cq_array = CircularQueueArray(5)

# Operations
cq_array.enqueue(1)  
cq_array.enqueue(2)  
cq_array.peek()      
cq_array.dequeue()   
cq_array.enqueue(3)  
cq_array.enqueue(4)  
cq_array.enqueue(5)  
cq_array.enqueue(6)  
cq_array.dequeue()  
cq_array.peek()      
cq_array.enqueue(7)  
cq_array.enqueue(8)  
cq_array.dequeue()   
cq_array.dequeue()   
cq_array.dequeue()   
cq_array.dequeue()   
cq_array.peek()      
cq_array.dequeue()  
cq_array.dequeue()   
cq_array.peek()      

# Initialize the circular queue for the linked list implementation
cq_linked_list = CircularQueueLinkedList()

# Operations 
cq_linked_list.enqueue(1)
cq_linked_list.enqueue(2)
cq_linked_list.peek()
cq_linked_list.dequeue()
cq_linked_list.enqueue(3)
cq_linked_list.enqueue(4)
cq_linked_list.enqueue(5)
cq_linked_list.enqueue(6)
cq_linked_list.dequeue()
cq_linked_list.peek()
cq_linked_list.enqueue(7)
cq_linked_list.dequeue()
cq_linked_list.dequeue()
cq_linked_list.dequeue()
cq_linked_list.dequeue()
cq_linked_list.peek()
cq_linked_list.dequeue()
cq_linked_list.dequeue()
cq_linked_list.peek()
