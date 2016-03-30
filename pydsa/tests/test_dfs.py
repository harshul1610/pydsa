from pydsa.dfs import dfs


def test_dfs():
    graph = {'A': ['B', 'C'],
             'B': ['A', 'D', 'E'],
             'C': ['A', 'F'],
             'D': ['B'],
             'E': ['B', 'F'],
             'F': ['C', 'E']}
    assert dfs(graph, 'A') == ['A', 'B', 'C', 'F', 'E', 'D']
