class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        edgeNum, j = 0, 0
        while len(edges) > 0:
            edge = edges.pop(0)
            head = edge[0]
            tail = edge[1]
            edgeNum += 1
            while j < len(edges):
                if edges[j][0] == tail:
                    head = edges[j][0]
                    tail = edges[j][1]
                    edges.pop(j)
                else:
                    j += 1

        return edgeNum

if __name__ == '__main__':
    sol = Solution()
    edges = [[0, 1], [1, 2], [3, 4]]
    assert (sol.countComponents(5, edges) == 2)

    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert (sol.countComponents(5, edges) == 1)

    edges = [[0, 1], [2, 3], [4, 5], [6, 7]]
    assert (sol.countComponents(8, edges) == 4)


