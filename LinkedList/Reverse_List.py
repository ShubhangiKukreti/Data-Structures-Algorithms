class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        current = self.head
        new_node = Node(new_value)
        if self.head:
            while current.next:
                current = current.next
            current.next = new_node

        else:
            self.head = new_node

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def reverse(self):
        if not self.head.next:
            return self.head.value
        else:
            current = self.head
            prev = second = None
            while current is not None:
                # we need to make sure that the entire list is not lost, so assign next to the second node before
                # swapping
                second = current.next
                # we point the current node towards the prev node
                current.next = prev
                # it is important to assign the previous node before the current node otherwise the address of the
                # current node will be lost
                prev = current
                current = second
            self.head = prev



ll = LinkedList()
ll.append(3)
ll.append(8)
ll.append(11)
ll.append(20)
print("list before")
ll.traverse()
ll.reverse()
print("list after")
ll.traverse()
