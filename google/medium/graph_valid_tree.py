# 261. Graph Valid Tree
# 
# Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), 
# 
# write a function to check whether these edges make up a valid tree.
# 
# For example:
# 
# Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.
# 
# Hint:
# 
# Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is this case a valid tree?

import collections
class Solution(object):
    def validTree(self, n, edges):
        adj = collections.defaultdict(list)
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)

        bfsque, visited = [], [0 for _ in range(n)]
        bfsque.append(0)
        while len(bfsque) > 0:
            i = bfsque.pop(0)
            visited[i] = 1
            for node in adj[i]:
                adj[node].remove(i)
                if visited[node]:
                    return False
                visited[node] = 1
                bfsque.append(node)
        return sum(visited) == n and len(edges) == n - 1

if __name__ == '__main__':
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    sol = Solution()
    assert sol.validTree(5, edges) == True

    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    assert sol.validTree(5, edges) == False

    edges = [[0, 1], [1, 2], [2, 0]]
    assert sol.validTree(5, edges) == False

    edges = [[0, 1], [1, 2], [3, 4]]
    assert sol.validTree(5, edges) == False

    edges = [[0, 1], [1, 2], [2, 3]]
    assert sol.validTree(4, edges) == True
        