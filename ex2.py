import timeit

#2.1: Implement a priority queue class based on Python arrays (ref. to the discussion in the lecture on queues) [0.3 pts]
    # The priority queue must implement enqueue by appending at the end of the array, 
    # and then immediately sorting the array using mergesort, and dequeue by removing the first element

class PriorityQueueSort:
    def __init__(self):
        self.queue = [] #class is initialized with an empty array

    def enqueue(self, item):
        self.queue.append(item) #appends an item to the emd of the self.queue array
        self._merge_sort(self.queue) #calls _merge_sort to sort the array using mergesort

    def dequeue(self): #removes and returns the first element from the queue
        if self.is_empty(): #checks if the queue is empty
            print("Queue is empty. Unable to dequeue item.") #if empty returns none
            return None
        return self.queue.pop(0)
    
    def is_empty(self): #returns a true or false value
        return len(self.queue) == 0 #checks if the queue is empty by checking if the lenght of the array is equal to 0
    
    def print_queue(self):
        print("Queue:", self.queue) #prints the queue
    
    @staticmethod
    def _merge_sort(arr): #this helper method takes arr as input
        if len(arr) > 1: #if the array lenght is greater than 1
            mid = len(arr) // 2 #it divides the array into two halves left and right
            left_half = arr[:mid]
            right_half = arr[mid:]

            PriorityQueueSort._merge_sort(left_half) #recursively sorts both halves using _merge_sort
            PriorityQueueSort._merge_sort(right_half)

            i = 0
            j = 0
            k = 0

            while i < len(left_half) and j < len(right_half): #checks which element is smaller and assigns then accordingly
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half): #copies any remaining elements in left and right to arr
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

# Example:
pq = PriorityQueueSort()
pq.enqueue(3)
pq.enqueue(1)
pq.enqueue(4)
pq.enqueue(2)

pq.print_queue()  # Print the current state of the queue

print("Dequeue:", pq.dequeue())  # Should dequeue 1
print("Dequeue:", pq.dequeue())  # Should dequeue 2

pq.print_queue()  # Print the current state of the queue after dequeuing

#2.2: Implement another priority queue class [0.3 pts]
    # The priority queue must implement enqueue by inserting the new element in 
    # the appropriate location to ensure the array remains sorted at all times, and dequeue by removing the first element

class PriorityQueueInsert:
    def __init__(self):
        self.queue = [] #initialize with empty array

    def enqueue(self, item):
        if not self.queue:
            self.queue.append(item)
        else:
            for i in range(len(self.queue)):
                if item <= self.queue[i]: #if item has equal or higher priority, insert it before element i
                    self.queue.insert(i, item)
                    return
            self.queue.append(item) #else append it to the end of the queue

    def dequeue(self): #same as previous class
        if self.is_empty():
            print("Queue is empty. Cannot dequeue item.")
            return None
        return self.queue.pop(0)
    
    def is_empty(self): #same as previous class
        return len(self.queue) == 0
    
    def print_queue(self):
        print("Queue1:", self.queue)

# Example:
pq1 = PriorityQueueInsert()
pq1.enqueue(3)
pq1.enqueue(1)
pq1.enqueue(4)
pq1.enqueue(2)

pq1.print_queue()  #print the current state of the queue

print("Dequeue:", pq1.dequeue())  #should dequeue 1
print("Dequeue:", pq1.dequeue())  #should dequeue 2

pq1.print_queue()  #print the current state of the queue after dequeuing

#2.3: Write a function which generates random lists of 1000 tasks. 
    # Each task is either an enqueue with probability 0.7, or a dequeue with probability 0.3

# What is the question asking for? (used external resources to understand the question)
# In this context, tasks are simply actions that represent operations on a queue. These tasks can be of two types: enqueue or dequeue.
    # An "enqueue" task represents adding an element to a queue.
    # A "dequeue" task represents removing an element from a queue.
    # Each task is represented by a string: "enqueue" or "dequeue".
    # The function create_random_tasks() should generate a list of 1000 such tasks, 
    # where each task is randomly chosen to be an enqueue operation with a probability of 0.7 or a dequeue operation with a probability of 0.3.

import random

def create_random_tasks():
    tasks = []
    for a in range(1000):
        if random.random() < 0.7: #enqueue with probability 0.7
            tasks.append("enqueue")
        else:
            tasks.append("dequeue") #dequeue with probabitlity 0.3
    return tasks

#So, the list of tasks generated by create_random_tasks() contains a sequence of these two types of tasks: "enqueue" and "dequeue". 
# Each task represents an operation that can be performed on a queue, and the sequence of tasks determines the order in which these operations will be performed.

#Usage
random_tasks = create_random_tasks()
print(random_tasks[:10]) #print 10 of the 1000 tasks

#2.4: Measure the performance of both implementations on 100 such lists using timeit and print the results

#create 100 random lists of tasks
lists_of_tasks = [create_random_tasks() for _ in range(100)]

#measure the performance of PriorityQueueInsert
time_insert = timeit.timeit(
    stmt = "for task in tasks: pq.enqueue(task)",
    setup = "from __main__ import PriorityQueueInsert, lists_of_tasks; pq = PriorityQueueInsert(); tasks = lists_of_tasks[0]",
    number = 100
)

#measure the performance of PriorityQueueSort
time_sort = timeit.timeit(
    stmt = "for task in tasks: pq.enqueue(task)",
    setup = "from __main__ import PriorityQueueSort, lists_of_tasks; pq = PriorityQueueSort(); tasks = lists_of_tasks[0]",
    number = 100
)

print("Time taken for PriorityQueueInsert:", time_insert)
print("Time taken for PriorityQueueSort:", time_sort)

#2.5: Discuss the results: which implementation is faster? Why?

#PriorityQueueInsert is faster then PriorityQueueSort because it inserts elements into the queue in a sorted 
#order directly, without performing a full sorting operation separately like in PriorityQueueSort.

#Complexities:
#PriorityQueueInsert: worst case -> O(n), where n is the number of elements in the queue. 
    # This class iterates over the queue to find where to insert the new element, so worst case it would have to iterate over the entire list

#PriorityQueueSort: worst case -> O(nlogn)
    # This class involves inserting a new element and sorting the entire queue using mergesort
    # mergesort has a worst case complexity of O(nlogn), so this methode would have the same worst case complexity

#Therefore, PriorityQueueInsert is more efficient and faster, especially as the size of the queue increases. 