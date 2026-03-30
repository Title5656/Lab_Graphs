def breadth_first_traversal(graph, start):
    visited = set()
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            print("Visiting:", node)
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)
    print("BFS complete")
    return visited

g1 = {
    'A': ['B','C','E'],
    'B': ['A','D'],
    'C': ['A','D','E'],
    'D': ['B','C'],
    'E': ['A','C']
}

breadth_first_traversal(g1,'B')