class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.stack) == 0:
            return "Queue is empty"
        temp_arr = []
        index = len(self.stack) - 1
        while index >= 0:
            temp_arr.append(self.stack[index])
            index -= 1
        temp = temp_arr[len(temp_arr) - 1]
        temp_arr.pop()
        self.stack = []
        index = len(temp_arr) - 1
        while index >= 0:
            self.stack.append(temp_arr[index])
            index -= 1
        return temp

    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.stack) == 0:
            return "Queue is empty"
        temp_arr = []
        index = len(self.stack) - 1
        while index >= 0:
            temp_arr.append(self.stack[index])
            index -= 1
        temp = temp_arr[len(temp_arr) - 1]
        return temp

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.stack) == 0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
