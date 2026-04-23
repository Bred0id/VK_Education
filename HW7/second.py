from collections import deque

def is_tree(graph, start):
    if not graph:
        return True
    
    visited = []
    queue = deque([start])
    parent = {start: None}

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                if parent.get(vertex) != neighbor:
                    return False
                
    return len(visited) == len(graph)