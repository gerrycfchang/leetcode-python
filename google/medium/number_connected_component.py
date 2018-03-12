# 323. Number of Connected Components in an Undirected Graph 
#
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# 
# write a function to find the number of connected components in an undirected graph.
# 
# Example 1:
# 
#      0          3
# 
#      |          |
# 
#      1 --- 2    4
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.
# 
# Example 2:
# 
#      0           4
# 
#      |           |
# 
#      1 --- 2 --- 3
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.
# 
#  Note:
# 
# You can assume that no duplicate edges will appear in edges. 
# Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

import collections
class Solution(object):
    def countComponents(self, n, edges):
        adj = collections.defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        bfsque, visited, count = [], [0 for _ in range(n)], 0

        while len(adj) > 0:
            newNode = sorted(adj.items(), key = lambda x: x[0])[0][0]
            bfsque.append(newNode)
            while len(bfsque) > 0:
                i = bfsque.pop(0)
                visited[i] = 1
                for node in adj[i]:
                    adj[node].remove(i)
                    if visited[node] == 0:
                        visited[node] = 1
                    if len(adj[node]) == 0:
                        del adj[node]
                    else:
                        bfsque.append(node)
                del adj[i]
            count += 1
        return count


if __name__ == '__main__':
    sol = Solution()
    edges = [[0, 1], [1, 2], [3, 4]]
    assert (sol.countComponents(5, edges) == 2)

    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert (sol.countComponents(5, edges) == 1)

    edges = [[0, 1], [2, 3], [4, 5], [6, 7]]
    assert (sol.countComponents(8, edges) == 4)

    edges = [[3, 2], [1, 2], [0, 1], [3, 4]]
    assert (sol.countComponents(8, edges) == 1)


