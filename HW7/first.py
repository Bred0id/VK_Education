def has_cycle(graph):
    visited = []
    
    def dfs(vertex, parent):
        visited.append(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor != parent:
                if neighbor in visited or dfs(neighbor, vertex):
                    return True
        return False

    for vertex in graph:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
            
    return False