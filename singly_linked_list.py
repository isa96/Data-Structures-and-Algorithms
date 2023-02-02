from typing import Any


class Node:
    def __init__(self, data: Any, next_node=None):
        self.data = data
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node: Node):
        if not isinstance(node, Node):
            node = Node(node)
        if self.head:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        else:
            self.head = node

    def extend(self, values):
        for v in values:
            self.append(v)

    def extend_flat(self, *args):
        for v in args:
            self.append(v)

    def insert(self, index: int, node: Node):
        if not isinstance(index, int):
            raise TypeError("index must be an integer bigger than 0")
        if index < 0:
            raise TypeError("index must be an integer bigger than 0")
        if not isinstance(node, Node):
            node = Node(node)
        if self.head is None:
            if index != 0:
                raise IndexError("Index out of range for empty linked list")
            else:
                self.head = node
                return

        curr_ix = 0
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                raise IndexError(
                    f"Index out of range for linked list (max index = {curr_ix})"
                )
            curr = curr.next
            curr_ix += 1

        node.next = curr.next
        curr.next = node

    def pop(self, index: int):
        if not isinstance(index, int):
            raise TypeError("index must be an integer bigger than 0")
        if index < 0:
            raise TypeError("index must be an integer bigger than 0")
        if index == 0:
            self.head = self.head.next
            return

        curr_ix = 0
        curr = self.head
        for _ in range(index - 1):
            if curr is None:
                raise IndexError(
                    f"Index out of range for linked list (max index = {curr_ix})"
                )
            curr = curr.next
            curr_ix += 1

        try:
            curr.next = curr.next.next
        except:
            raise IndexError(
                f"Index out of range for linked list (max index = {curr_ix})"
            )

    def reverse(self):
        if self.head:
            prev = None
            curr = self.head
            while curr is not None:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            self.head = prev
            return
        raise AttributeError("Empty linked list doesn't have reverse method")

    def __repr__(self):
        res = []
        if self.head:
            curr = self.head
            while curr is not None:
                res.append(curr.data)
                curr = curr.next
        return str(res)


if __name__ == "__main__":
    linked_list = LinkedList()

    print(linked_list)
    linked_list.append(Node(2))
    linked_list.extend([4, 10])
    print(linked_list)
    linked_list.pop(2)
    linked_list.pop(1)
    print(linked_list)
    linked_list.extend_flat(4, 10)
    print(linked_list)

    linked_list.insert(1, Node(213))
    print(linked_list)
    linked_list.reverse()
    print(linked_list)
    linked_list.pop(3)
    print(linked_list)
    try:
        linked_list.pop(3)
    except Exception as e:
        print(e)
    linked_list.pop(1)
    print(linked_list)
    linked_list.pop(0)
    print(linked_list)
    linked_list.pop(1)
    print(linked_list)
