class Stack:
    def __init__(self):
        self.array= []

    def peek(self):
        if len(self.array) == 0:
            print("Stack is empty")
        else:
            return self.array[len(self.array) - 1]

    def push(self, value):
        self.array.append(value)

    def pop(self):
        if len(self.array) == 0:
            print("Stack is empty!")
        else:
            self.array.pop()

    def traverse(self):
        index = len(self.array )- 1
        while index >= 0:
            print(self.array[index])
            index -= 1

mystack = Stack()
mystack.push(7)
mystack.push(8)
mystack.push(4)
print(mystack.peek())
mystack.pop()
print("full stack")
# print(mystack.length)
# print(mystack.top)
mystack.traverse()
