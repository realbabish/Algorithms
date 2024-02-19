class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if len(self.items) == 0:
            return print("Queue is empty")
        return print("Queue is not empty")

    def enqueue(self, value):
        self.items.append(value)

    def deque(self):
        del self.items[0]

    def top_element(self):
        index = len(self.items) - 1
        return print("The top element of the queue is: ", self.items[index])

    def peek(self):
        return print("The bottom of the queue ; First Element is: ", self.items[0])

    def length(self):
        index = len(self.items)
        return print("The number of units in the queue is: ", index)


Queue = Queue()
print(Queue.is_empty())
print("------Queue after enquing 6 elements------")

Queue.enqueue(1)
Queue.enqueue(2)
Queue.enqueue(3)
Queue.enqueue(4)
Queue.enqueue(5)
Queue.enqueue(6)

print(Queue.top_element())
print(Queue.peek())

print("------Queue after dequeueing 2 elements------")
Queue.deque()
Queue.deque()
print(Queue.top_element())
print(Queue.peek())
print(Queue.length())
