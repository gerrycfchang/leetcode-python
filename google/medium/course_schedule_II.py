"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
Another correct ordering is[0,2,1,3].

"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        indegree = [0 for i in range(numCourses)]
        conn = {i: [] for i in range(numCourses)}
        zero_indegree = []

        for link in prerequisites:
            indegree[link[1]] += 1
            conn[link[0]].append(link[1])

        for i in range(len(indegree)):
            if indegree[i] == 0:
                zero_indegree.append(i)
        i = 0
        while i < len(zero_indegree):
            for node in conn[zero_indegree[i]]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    zero_indegree.append(node)
            i += 1

        if len(zero_indegree) == numCourses:
            return zero_indegree[::-1]
        else:
            return []

if __name__ == '__main__':
    sol = Solution()
    courses = [[1,0]]
    assert (sol.findOrder(2, courses) == [0, 1])

    courses = [[1,0],[2,0],[3,1],[3,2]]
    assert (sol.findOrder(4, courses) == [0,2,1,3])