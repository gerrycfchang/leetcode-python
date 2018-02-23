"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        indegree = [0 for i in range(numCourses)]
        conn = {i: [] for i in range(numCourses)}
        zero_indegree = []
        for link in prerequisites:
            conn[link[0]].append(link[1])
            indegree[link[1]] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                zero_indegree.append(i)
        i = 0
        while i < len(zero_indegree):
            for node in conn[zero_indegree[i]]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1
        return len(zero_indegree) == numCourses

if __name__ == '__main__':
    sol = Solution()
    courses = [[1,0]]
    assert (sol.canFinish(2, courses) == True)

    courses = [[0, 1]]
    assert (sol.canFinish(2, courses) == True)

    courses = [[1, 0],[0, 1]]
    assert (sol.canFinish(2, courses) == False)
    
    courses = [[1, 0],[0, 4],[4, 3], [3, 2], [4, 2]]
    assert (sol.canFinish(5, courses) == True)        




