# Depth First Search
# Complexity: O(V+E)

def dfs(graph,s):
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

graph = {'A':['B', 'C'],
         'B':['A', 'D', 'E'],
         'C':['A', 'F'],
         'D':['B'],
         'E':['B', 'F'],
         'F':['C', 'E']}
print dfs(graph,'A')