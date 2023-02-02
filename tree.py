from queue import Queue


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, node: Node):
        self.node = node

    def preorder(self):
        print("Preorder traversal")
        print(self.__preorder(self.node))

    def __preorder(self, node: Node):
        res = []
        res.append(node.data)
        if node.left:
            res += self.__preorder(node.left)
        if node.right:
            res += self.__preorder(node.right)
        return res

    def inorder(self):
        print("Inorder traversal")
        print(self.__inorder(self.node))

    def __inorder(self, node: Node):
        res = []
        if node.left:
            res += self.__inorder(node.left)
        res.append(node.data)
        if node.right:
            res += self.__inorder(node.right)
        return res

    def postorder(self):
        print("Postorder traversal")
        print(self.__postorder(self.node))

    def __postorder(self, node: Node):
        res = []
        if node.left:
            res += self.__postorder(node.left)
        if node.right:
            res += self.__postorder(node.right)
        res.append(node.data)
        return res

    def bfs(self):
        queue = Queue()
        queue.enqueue(self.node)
        res = []
        while len(queue) > 0:
            curr = queue.dequeue()
            res.append(curr.data)
            if curr.left:
                queue.enqueue(curr.left)
            if curr.right:
                queue.enqueue(curr.right)
        print("BFS traversal")
        print(res)


if __name__ == "__main__":

    n = Node(25)
    n.left = Node(15)
    n.left.left = Node(10)
    n.left.left.left = Node(4)
    n.left.left.right = Node(12)
    n.left.right = Node(22)
    n.left.right.left = Node(18)
    n.left.right.right = Node(24)
    n.right = Node(50)
    n.right.left = Node(35)
    n.right.left.left = Node(31)
    n.right.left.right = Node(44)
    n.right.right = Node(70)
    n.right.right.left = Node(66)
    n.right.right.right = Node(90)

    tree = Tree(n)
    tree.inorder()
    tree.preorder()
    tree.postorder()
    tree.bfs()
