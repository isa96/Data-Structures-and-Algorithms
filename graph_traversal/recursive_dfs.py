from typing import List, Dict, Any

def dfs(
    graph: Dict[Any, List[Any]], 
    start: Any, 
    visited: List[Any] = None,
) -> List[Any]:
    if visited is None:
        visited = []
    visited.append(start)
    print(f"visiting: {start}")
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            visited = dfs(graph, neighbor, visited)

    return visited


if __name__ == "__main__":
    graph = {
        "a": ["b", "c", "d"],
        "b": ["i", "a"],
        "c": ["x"]
    }

    dfs(graph, "a")