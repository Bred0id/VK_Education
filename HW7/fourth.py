from collections import deque

def is_bipartite(graph):
    n = len(graph)
    colors = [0] * n

    def bfs(start):
        queue = deque([start])
        colors[start] = 1
        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if colors[neighbor] == 0:
                    colors[neighbor] = -colors[node]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[node]:
                    return False
        return True

    for i in range(n):
        if colors[i] == 0:
            if not bfs(i):
                return False
            
    return True