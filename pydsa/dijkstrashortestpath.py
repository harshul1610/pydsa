import heapq
import sys



def dijkstra(graph,source_node,target_node):
    visited = dict()
    distance = dict()
    previous = dict()
    paths = list()
    for node in graph:
        distance[node] = sys.maxsize
        previous[node] = None
        visited[node] = False
    distance[source_node] = 0
    #define priority queue
    pqueue = [(distance[node],node) for node in graph]
    heapq.heapify(pqueue)
    while(len(pqueue) > 0):
        v = heapq.heappop(pqueue)
        visited[v[1]] = True
        for adjnode in graph[v[1]]:
            if visited[adjnode[0]] == True:
                continue
            if distance[adjnode[0]] > distance[v[1]]+int(adjnode[1]):
                distance[adjnode[0]]=distance[v[1]]+int(adjnode[1])
                previous[adjnode[0]] = v[1]
        for i in range(len(pqueue)):
            heapq.heappop(pqueue)
        pqueue = [(distance[node],node) for node in graph if visited[node] is False]
        heapq.heapify(pqueue)

    while True:
        if target_node == source_node:
            paths.append(target_node)
            return paths[::-1]
        else:
            paths.append(target_node)
            target_node=previous[target_node]


    #print 'Distance:' , distance
    #print 'Previous:' , previous



