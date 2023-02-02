class Stack(list):
    def __init__(self, values=[]):
        super().__init__(values)

    def pop(self):
        return super().pop()

    def dequeue(self):
        return self.pop()

    def enqueue(self, value):
        super().append(value)


if __name__ == "__main__":
    stack = Stack([1, 2, 3])

    stack.enqueue("a")
    print(stack)
    print(stack.dequeue())
    print(stack)
    print(stack.pop())
