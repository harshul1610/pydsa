from pydsa.dfs import dfsearch

def test_dfs():
    graph = {'A':['B', 'C'],
             'B':['A', 'D', 'E'],
             'C':['A', 'F'],
             'D':['B'],
             'E':['B', 'F'],
             'F':['C', 'E']}
    assert dfsearch(graph, 'A') == ['A', 'B', 'C', 'F', 'E', 'D']
