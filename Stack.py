class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        print(len(self.items) == 0)
        return len(self.items) == 0

    def push(self, value):
        self.items.append(value)

    def pop(self):
        index = len(self.items) - 1
        del self.items[index]

    def top_element(self):
        index = len(self.items) - 1
        return print("The top element of the stack is: ", self.items[index])
    def peek(self):
        return print("The bottom of the stack ; First Element is: ", self.items[0])

    def length(self):
        index = len(self.items)
        return print("The number of units in the stack is: ", index)


Stack = Stack()
Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(4)
Stack.push(5)
Stack.push(6)

print("Stack after 6 pushes")
Stack.peek()
Stack.top_element()
Stack.length()

print("Top of the stack after a pop")
Stack.pop()
Stack.peek()
Stack.top_element()
Stack.length()

print("Top of the stack after the 2nd pop")
Stack.pop()
Stack.peek()
Stack.top_element()
Stack.length()


