from typing import List, Dict, Tuple, Set, Any

def bfs(
    graph: Dict[Any, List[Any]], 
    start: Any, 
    queue: List[Any] = None,
    visited: Set[Any] = None,
) -> Tuple[List[Any], List[Any]]:
    if queue is None:
        queue = []
    if visited is None:
        visited = set()
    visited.add(start)
    print(f"visiting: {start}")
    
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            queue.append(neighbor)

    try:
        nxt = queue.pop(0)
    except:
        return queue, visited
    queue, visited = bfs(graph, nxt, queue, visited)

    return queue, visited


if __name__ == "__main__":
    graph = {
        "a": ["b", "c", "d"],
        "b": ["i", "a"],
        "c": ["x"]
    }

    bfs(graph, "a")