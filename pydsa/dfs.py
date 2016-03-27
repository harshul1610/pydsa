# Depth First Search
# Complexity: O(V+E)

def dfsearch(graph,s):
    stack = list()
    visited=list()
    stack.append(s)
    visited.append(s)
    while(len(stack)>0):
        node = stack.pop()
        for subadjnode in graph[node]:
            if subadjnode not in visited:
                visited.append(subadjnode)
                stack.append(subadjnode)
    return visited