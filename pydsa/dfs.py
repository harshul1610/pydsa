
def dfs(graph,s):
    stack = list()
    visited=list()
    stack.append(s)
    while(len(stack)>0):
        node = stack.pop()
        visited.append(node)
        for subadjnode in graph[node]:
            if subadjnode not in visited:
                stack.append(subadjnode)
    return visited
