class Queue(list):
    def __init__(self, values=[]):
        super().__init__(values)

    def pop(self):
        return super().pop(0)

    def dequeue(self):
        return self.pop()

    def enqueue(self, value):
        super().append(value)


if __name__ == "__main__":
    queue = Queue([1, 2, 3])

    queue.enqueue("a")
    print(queue)
    print(queue.dequeue())
    print(queue)
    print(queue.pop())
