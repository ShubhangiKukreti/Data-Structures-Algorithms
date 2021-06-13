class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.length == 0:
            return "Queue is empty!"
        return self.first.value

    def enqueue(self, new_value):
        new_node = Node(new_value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return "The queue is empty"
        if self.first == self.last:
            self.last = None
        self.first = self.first.next
        self.length -= 1


my_queue = Queue()

my_queue.enqueue(6)
my_queue.enqueue(4)
my_queue.enqueue(8)
my_queue.enqueue(9)

print(my_queue.length)
print(my_queue.peek())
my_queue.dequeue()

print(my_queue.length)
