class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def append(self, new_value):
        current = self.head
        new_node = Node(new_value)
        if self.head:
            while current.next:
                # we are using current.next in the while loop because we want to reach till he last element.
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
        # complexity: O(n)

    def append_using_tail(self, new_value):
        new_node = Node(new_value)
        if self.head:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        # complexity:O(1)

    def prepend(self, new_value):
        current = self.head
        new_node = Node(new_value)
        if self.head:
            self.head = new_node
            new_node.next = current
        else:
            self.head = new_node
        # complexity:O(1)

    def traverse(self):
        current = self.head
        while current:
            # we can't use current.next in this loop because even though we reach the last element, the value won't be
            # printed because the condition for the loop is not satisfied.
            print(f"The value stored is {current.value}")
            current = current.next
    # complexity O(n)

    def insert(self, index, new_value):
        # TO DO: add validation for indexes
        current = self.head
        new_node = Node(new_value)
        if index == 0:
            self.head = new_node
            new_node.next = current
        else:
            count = 1
            while count < (index - 1):
                current = current.next
                count += 1
            new_node.next = current.next
            current.next = new_node

    def remove(self, index):
        count = 1
        current = self.head
        if index == 0:
            self.head = current.next
        else:
            while count < (index - 1):
                current = current.next
            current.next = current.next.next


linked_list = LinkedList()
# linked_list2 = LinkedList()

linked_list.append(5)
linked_list.append(6)
linked_list.append(9)
linked_list.append(8)
print("Linked list before")
linked_list.traverse()

linked_list.remove(0)

print("Linked list using append using tail")
linked_list.traverse()

