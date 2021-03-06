# 797. All Paths From Source to Target
#
# Given a directed, acyclic graph of N nodes.  
# 
# Find all possible paths from node 0 to node N-1, and return them in any order.
# 
# The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  
# 
# graph[i] is a list of all nodes j for which the edge (i, j) exists.
# 
# Example:
# Input: [[1,2], [3], [3], []] 
# Output: [[0,1,3],[0,2,3]] 
# Explanation: The graph looks like this:
# 0--->1
# |    |
# v    v
# 2--->3
# There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(curr, path):
            if curr == len(graph) - 1: res.append(path)
            else:
                for i in graph[curr]:
                    dfs(i, path + [i])
        res = []
        dfs(0, [0])
        return res

if __name__ == '__main__':
    sol = Solution()
    graph = [[1,2], [3], [3], []]
    exp = [[0,1,3],[0,2,3]]
    assert sol.allPathsSourceTarget(graph) == exp

