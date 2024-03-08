import random
import timeit
import matplotlib.pyplot as plt

# Q1

class ArrayStack:
    def __init__(self):
        self.array = []
    
    def push(self, element):
        self.array.append(element)
    
    def pop(self):
        if not self.array:
            raise IndexError("pop from empty stack")
        return self.array.pop()
    
    def is_empty(self):
        return len(self.array) == 0 # if empty create an Arraystack

# Q2
    
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedListStack:
    def __init__(self):
        self.head = None
    
    def push(self, element):
        new_node = Node(element)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if not self.head:
            raise IndexError("pop from empty stack")
        value = self.head.value
        self.head = self.head.next
        return value
    
    def is_empty(self):
        return self.head is None #if empty create a LinkedListStack

# Q3
    
def generate_tasks(n=10000):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:  # 70% probability for push
            tasks.append(('push', random.randint(1, 100))) 
        else:  # 30% probability for pop
            tasks.append(('pop',))
    return tasks

# Q4

def perform_tasks(tasks, stack):
    for task in tasks:
        if task[0] == 'push':
            stack.push(task[1])
        elif task[0] == 'pop':
            if not stack.is_empty(): 
                stack.pop()
                
def measure_performance(stack_class):
    times = []
    for _ in range(100):  # Generate and measure 100 lists of tasks
        tasks = generate_tasks()
        stack = stack_class()
        start_time = timeit.default_timer()
        perform_tasks(tasks, stack)
        times.append(timeit.default_timer() - start_time)
    return times

array_stack_times = measure_performance(ArrayStack)
linked_list_stack_times = measure_performance(LinkedListStack)

# Q5

plt.plot(array_stack_times, alpha=0.5, label='ArrayStack')
plt.plot(linked_list_stack_times, alpha=0.5, label='LinkedListStack')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend(loc='upper right')
plt.title('Performance of Stack Implementations')
plt.show()
