from typing import Union
from queue import Queue
from stack import Stack
from priority_queue import PriorityQueue


class Node:
    def __init__(self, name):
        self.name = name
        self.vertices = []

    def add_vertex(self, vertex):
        if vertex in self.vertices:
            # raise ValueError(f"Can't add duplicate vertex to node `{self.name}`")
            return
        self.vertices.append(vertex)


class Vertex:
    def __init__(self, target, weight=1):
        if not isinstance(target, Node):
            raise TypeError("Expecting Node object for argument `target`")
        self.target = target
        self.weight = weight


class Graph:
    def __init__(self):
        self.__nodes = {}

    def add_node(self, node: Node) -> None:
        if not isinstance(node, Node):
            raise TypeError("Expecting Node object for argument `node`")
        name = node.name
        if self.__nodes.get(name):
            # raise ValueError(f"`{name}` already in graph")
            return
        self.__nodes[name] = node

    def add_vertex(
        self,
        source: Node,
        target: Node,
        weight: Union[int, float] = 1,
        is_directed: bool = False,
    ) -> None:
        if not is_directed:
            target.add_vertex(Vertex(source, weight))
        source.add_vertex(Vertex(target, weight))

        self.add_node(source)
        self.add_node(target)

    def bfs(self, start: str, stop: str) -> None:
        if self.__nodes.get(start) is None:
            raise ValueError(f"Can't find start `{start}` in graph")
        if self.__nodes.get(stop) is None:
            raise ValueError(f"Can't find stop `{stop}` in graph")

        queue = Queue()
        queue.enqueue((0, self.__nodes[start], []))  # [(distance, curr, visited)]
        while len(queue) > 0:
            distance_traveled, curr, visited = queue.dequeue()
            print(f"Visiting {curr.name} (travel distance = {distance_traveled} km)")
            if curr.name == stop:
                print(f"Reached final destination")
                return
            for vertex in curr.vertices:
                if vertex.target in visited:
                    continue
                queue.enqueue(
                    (distance_traveled + vertex.weight, vertex.target, visited + [curr])
                )

        print("No path found")

    def dfs(self, start: str, stop: str) -> None:
        if self.__nodes.get(start) is None:
            raise ValueError(f"Can't find start `{start}` in graph")
        if self.__nodes.get(stop) is None:
            raise ValueError(f"Can't find stop `{stop}` in graph")

        stack = Stack()
        stack.enqueue((0, self.__nodes[start], []))  # [(distance, curr, visited)]
        while len(stack) > 0:
            distance_traveled, curr, visited = stack.dequeue()
            print(f"Visiting {curr.name} (travel distance = {distance_traveled} km)")
            if curr.name == stop:
                print(f"Reached final destination")
                return
            for vertex in curr.vertices:
                if vertex.target in visited:
                    continue
                stack.enqueue(
                    (distance_traveled + vertex.weight, vertex.target, visited + [curr])
                )

        print("No path found")

    def djikstra(self, start: str, stop: str) -> None:
        if self.__nodes.get(start) is None:
            raise ValueError(f"Can't find start `{start}` in graph")
        if self.__nodes.get(stop) is None:
            raise ValueError(f"Can't find stop `{stop}` in graph")

        visited = set()
        visited.add(self.__nodes[start])
        priority_queue = PriorityQueue(key=lambda x: x[0])
        priority_queue.enqueue((0, self.__nodes[start]))  # [(distance, curr)]
        while len(priority_queue) > 0:
            distance_traveled, curr = priority_queue.dequeue()
            print(f"Visiting {curr.name} (travel distance = {distance_traveled} km)")
            if curr.name == stop:
                print(f"Reached final destination")
                return
            for vertex in curr.vertices:
                if vertex.target in visited:
                    continue
                priority_queue.enqueue(
                    (distance_traveled + vertex.weight, vertex.target)
                )
                visited.add(vertex.target)

        print("No path found")


if __name__ == "__main__":
    g = Graph()

    frankfurt = Node("Frankfurt")
    mannheim = Node("Mannheim")
    wurzburg = Node("Wurzburg")
    stuttgart = Node("Stuttgart")
    kassel = Node("Kassel")
    karlshure = Node("Karlshure")
    ertfurt = Node("Ertfurt")
    nurnberg = Node("Nurnberg")
    augsburg = Node("Augsburg")
    muenchen = Node("Muenchen")

    avaiable_paths = [
        (frankfurt, mannheim, 85),
        # (frankfurt, wurzburg, 217),
        (frankfurt, kassel, 173),
        (mannheim, karlshure, 80),
        (karlshure, augsburg, 250),
        (augsburg, muenchen, 84),
        (wurzburg, ertfurt, 186),
        (wurzburg, nurnberg, 103),
        (nurnberg, stuttgart, 183),
        (nurnberg, muenchen, 167),
        (kassel, muenchen, 502),
    ]

    for target, source, distance in avaiable_paths:
        g.add_vertex(target, source, distance)

    g.add_node(Node("Jakarta"))

    g.bfs("Frankfurt", "Ertfurt")
    g.dfs("Frankfurt", "Ertfurt")
    g.djikstra("Frankfurt", "Ertfurt")

    g.djikstra("Jakarta", "Muenchen")
