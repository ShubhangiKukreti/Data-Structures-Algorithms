class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def pop(self):
        if self.length == 0:
            print("stack is empty!")
        elif self.top == self.bottom:
            self.bottom = None
            self.length -= 1
        else:
            current = self.top.next
            self.top = current
            self.length -= 1

    def push(self, new_value):
        new_node = Node(new_value)
        if self.top is None:
            self.top = new_node
            self.bottom = new_node
        else:
            temp = self.top
            self.top = new_node
            self.top.next = temp
        self.length += 1

    def peek(self):
        if self.length == 0:
            print("The stack is empty!")
        else:
            print(self.top.value)

    def traverse(self):
        if self.top is None:
            print("stack is empty")
        else:
            current = self.top
            while current:
                print(current.value)
                current = current.next


stack = Stack()
stack.push(8)
stack.push(4)
stack.push(9)
stack.push(7)
print(stack.peek())
print("the full stack")
stack.traverse()
stack.pop()
print("the full stack")
stack.traverse()
