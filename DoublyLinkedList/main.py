class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:
            self.head = self.tail = new_node
        self.length += 1

    def traverse_from_head(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def traverse_from_tail(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev

    def prepend(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.length += 1

    def insert(self, index, new_value):
        count = 1
        current = self.head
        new_node = Node(new_value)
        if self.head:
            if index == 0:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            else:
                while count < (index - 1):
                    current = current.next
                    count += 1
                new_node.next = current.next
                current.next.prev = new_node
                current.next = new_node
                new_node.prev = current
        else:
            self.head = new_node
            self.tail = new_node
        self.length += 1

    def remove(self, index):
        count = 1
        current = self.head
        if self.head:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
            elif index == self.length:
                self.tail = self.tail.prev
                self.tail.prev = None
            else:
                while count < index:
                    current = current.next
                    count += 1
                current.prev.next = current.next
                current.next.prev = current.prev
            self.length -= 1
        else:
            print("The linked list is empty!!")


ll = DoublyLinkedList()
ll.append(2)
ll.append(4)
ll.append(8)
ll.append(6)
# ll.prepend(7)
ll.insert(0,1)
print("before delete")
ll.traverse_from_head()
ll.remove(4)
print("after remove")
ll.traverse_from_head()



