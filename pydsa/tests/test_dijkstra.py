from pydsa.dijkstra import dijkstra


def test_dijkstra():
    graph = {'A': [('B', '2'), ('C', '1')],
             'B': [('A', '3'), ('D', '4'), ('E', '2')],
             'C': [('A', '1'), ('F', '4')],
             'D': [('B', '8')],
             'E': [('B', '0'), ('F', '6')],
             'F': [('C', '4'), ('E', '7')]}

    assert dijkstra(graph, 'A', 'E') == ['A', 'B', 'E']
