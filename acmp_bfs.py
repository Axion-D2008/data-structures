from collections import deque

def bfs(graph, start, end):
    visited = set()
    q = deque([[start]])

    if start == end:
        return [start]

    while q:
        path = q.popleft()
        node = path[-1]

        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                q.append(new_path)
                
                if neighbor == end:
                    return new_path
            visited.add(node)
    return None

g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2, 6],
    6: [3, 5]
}

print(bfs(g, 1, 6))
