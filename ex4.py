import random
import timeit
import matplotlib.pyplot as plt

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
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.is_empty():
            data = self.head.data
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return data
        else:
            print("Queue is empty. Unable to dequeue item.")
            return None

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

aq = ArrayQueue()
aq.enqueue(1)
aq.enqueue(3)
aq.enqueue(5)
aq.enqueue(2)
aq.enqueue(4)

#4.3:
    
def generate_random_tasks():
    tasks = []
    has_enqueued = False  # Flag to track if an enqueue task has been added
    for i in range(1000):
        if not has_enqueued:  # Ensure at least one enqueue task before dequeue
            tasks.append("enqueue")
            has_enqueued = True
        elif random.random() < 0.7:  # Enqueue with probability 0.7
            tasks.append("enqueue")
        else:  # Dequeue with probability 0.3
            tasks.append("dequeue")
    return tasks

def measure_performance(queue_class):
    setup_code = '''
from __main__ import generate_random_tasks, {}
tasks = generate_random_tasks()
queue = {}()
    '''.format(queue_class.__name__, queue_class.__name__)

    try:
        time_taken = timeit.timeit(
            stmt='''for task in tasks:
    if task == "enqueue":
        queue.enqueue(1)
    else:
        queue.dequeue()''',
            setup=setup_code,
            number=100
        )
    except IndexError as e:
        print(f"Encountered an IndexError: {e}")
        time_taken = None
    
    return time_taken

# Measure performance of ArrayQueue
array_times = [measure_performance(ArrayQueue) for _ in range(100)]

# Measure performance of LinkedListQueue
linked_list_times = [measure_performance(LinkedListQueue) for _ in range(100)]

# Plotting the distribution of times
plt.plot(array_times, label='ArrayQueue')
plt.plot(linked_list_times, label='LinkedListQueue')
plt.xlabel('List of Tasks')
plt.ylabel('Time Taken (seconds)')
plt.title('Performance Comparison of ArrayQueue and LinkedListQueue')
plt.legend()
plt.show()

#4.5: 

#For some lists of tasks, LinkedListQueue outperforms ArrayQueue, while for others, it may be the other way around.
#The variability in performance can be attributed to the inherent differences between array-based and linked list-based implementations.
# Arrays offer constant-time random access, making them efficient for certain operations like indexing, but resizing the array can be costly in terms of time complexity.
# Linked lists, while more flexible in terms of resizing and insertion/deletion at the ends, may incur additional overhead due to traversal and pointer manipulation.