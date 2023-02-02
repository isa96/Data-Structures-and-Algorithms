class PriorityQueue(list):
    def __init__(self, values=[], key=lambda x: x):
        self.key = key
        values.sort(key=self.key)
        super().__init__(values)

    def pop(self):
        return super().pop(0)

    def dequeue(self):
        return self.pop()

    def enqueue(self, value):
        target = self.key(value)

        if self.__len__() == 0:
            super().append(value)
            return

        # binary insertion
        low = 0
        if target <= self.key(self.__getitem__(low)):
            super().insert(low, value)
            return

        high = super().__len__() - 2
        while low <= high:
            mid = low + (high - low) // 2
            m0 = self.key(super().__getitem__(mid))
            m1 = self.key(self.__getitem__(mid + 1))
            # print(low, mid, high, value, m0, m1)
            if target > m0 and target <= m1:
                super().insert(mid + 1, value)
                return
            elif target <= m0:
                high = mid - 1
            else:
                low = mid + 1

        super().append(value)

    def extend(self, arr):
        for value in arr:
            self.enqueue(value)


if __name__ == "__main__":
    priority_queue = PriorityQueue([("abc", 2), ("def", 0)], key=lambda x: x[1])

    priority_queue.enqueue(("lmnop", 1))
    print(priority_queue)
    print(priority_queue.dequeue())
    priority_queue.enqueue(("efgh", 1))
    priority_queue.enqueue(("fff", 1))
    priority_queue.enqueue(("ggg", 1))
    print(priority_queue)
    priority_queue.enqueue(("wer", 2))
    priority_queue.enqueue(("fds", 2))
    print(priority_queue)
    priority_queue.enqueue(("ggfggg", 2))
    priority_queue.enqueue(("gf", 100))
    priority_queue.enqueue(("fdd", 2))
    priority_queue.enqueue(("xxx", 30))
    print(priority_queue)
    print(priority_queue.pop())

    priority_queue = PriorityQueue()
    print(priority_queue)
    priority_queue.enqueue((2, 10))
    print(priority_queue)
    priority_queue.enqueue((12, 10))
    print(priority_queue)
