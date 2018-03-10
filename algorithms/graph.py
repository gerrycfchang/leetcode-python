from heapq import heappush, heappop
class Dijkstra(object):
    def shortestPath(self, current, graph):
        inf = float('inf')
        unvisited = {key: inf for key in graph.keys()}
        visited, currentDistance = {}, 0

        while unvisited:
            for neighbor, distance in graph[current].items():
                if neighbor not in unvisited: continue
                newDistance = currentDistance + distance
                if unvisited[neighbor] > newDistance:
                    unvisited[neighbor] = newDistance
            visited[current] = currentDistance
            del unvisited[current]
            if not unvisited: break
            # get the smallest distance from unvisited nodes
            current, currentDistance = sorted(unvisited.items(), key = lambda x: x[1])[0]
        return visited
    
    def shortestPathWithPQ(self, current, graph):        
        visited = {key: None for key in graph.keys()}
        queue = [(0, current)]
        while queue:
            path_len, v = heappop(queue)
            if visited[v] == None: # v is unvisited
                visited[v] = path_len
                for w, edge_len in graph[v].items():
                    if visited[w] == None:
                        heappush(queue, (path_len + edge_len, w))          
        return visited

class MinSpanningTree(object):
    def construct(self, start, graph):
        visited = {key: None for key in graph.keys()}
        queue = [(0, start)]
        while queue:
            path, v = heappop(queue)
            if visited[v] == None:
                visited[v] = path
                for w, edge in graph[v].items():
                    if visited[w] == None:
                        heappush(queue, (edge, w))
        return visited

if __name__ == '__main__':
    graph = {'a': {'b': 14, 'c': 9, 'd': 7},
             'b': {'a': 14, 'c': 2, 'e': 9},
             'c': {'a': 9, 'b': 2, 'd': 10, 'f': 11},
             'd': {'a': 7, 'c': 10, 'f': 15},
             'e': {'b': 9, 'f': 6},
             'f': {'c': 11, 'd': 15, 'e': 6}}

    dij = Dijkstra()
    path = dij.shortestPath('a', graph)
    exp  = {'a': 0, 'c': 9, 'b': 11, 'e': 20, 'd': 7, 'f': 20}
    assert exp == path

    path = dij.shortestPathWithPQ('a', graph)
    assert exp == path

    mst = MinSpanningTree()
    tree = mst.construct('a', graph)
    exp  = {'a': 0, 'c': 9, 'b': 2, 'e': 9, 'd': 7, 'f': 6}
    assert exp == tree

    graph = { 'a': {'b': 4, 'h': 8},
              'b': {'a': 4, 'c': 8, 'h': 11},
              'c': {'b': 8, 'd': 7, 'f': 4, 'i': 2},
              'd': {'c': 7, 'e': 9, 'f': 14},
              'e': {'d': 9, 'f': 10},
              'f': {'c': 4, 'd': 14, 'e': 10, 'g': 2},
              'g': {'f': 2, 'h': 1, 'i': 6},
              'h': {'a': 8, 'b': 11, 'g': 1, 'i': 7},
              'i': {'c': 2, 'g': 6, 'h': 7}
            }
    tree = mst.construct('a', graph)
    exp  = {'a': 0, 'c': 8, 'b': 4, 'e': 9, 'd': 7, 'g': 2, 'f': 4, 'i': 2, 'h': 1}
    cost = sum(tree.values())
    assert exp == tree
    assert cost == 37

