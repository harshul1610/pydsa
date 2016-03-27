# Depth First Search
# Complexity: O(V+E)
# uses stack


def dfs(graph, start):
    stack = list()
    visited = list()
    stack.append(start)
    visited.append(start)
    while len(stack) > 0:
        node = stack.pop()
        for subadjnode in graph[node]:
            if subadjnode not in visited:
                visited.append(subadjnode)
                stack.append(subadjnode)
    return visited
