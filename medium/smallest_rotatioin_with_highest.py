# 798. Smallest Rotation with Highest Score
# 
# Given an array A, we may rotate it by a non-negative integer K so that the array 
# becomes A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1].  
# Afterward, any entries that are less than or equal to their index are worth 1 point. 
# 
# For example, if we have [2, 4, 1, 3, 0], and we rotate by K = 2, it becomes [1, 3, 0, 2, 4].  
# This is worth 3 points because 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point].
# 
# Over all possible rotations, return the rotation index K that corresponds to the highest score we could receive.  
# If there are multiple answers, return the smallest such index K.
# 
# Example 1:
# Input: [2, 3, 1, 4, 0]
# Output: 3
# Explanation:  
# Scores for each K are listed below: 
# K = 0,  A = [2,3,1,4,0],    score 1
# K = 1,  A = [3,1,4,0,2],    score 3
# K = 2,  A = [1,4,0,2,3],    score 3
# K = 3,  A = [4,0,2,3,1],    score 4
# K = 4,  A = [0,2,3,1,4],    score 3
# 
import collections
class Solution(object):
    def bestRotation(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        m = len(A)
        scores = [0 for _ in range(m)]
        for k in range(m):
            score = 0
            for i in range(m):
                index = i-k if i-k >=0 else i-k+m                    
                if A[i] <= index:
                    score += 1
            scores[k] = score
        return scores.index(max(scores))

    def bestRotationNoTLE(self, A):
        N = len(A)        
        arr = [A[i]-i for i in range(N)]        
        counter = collections.Counter(arr)
        max_points = 0
        for k in counter:
            if k<=0:
                max_points += counter[k]        
        ret = 0        
        points = max_points
        for i in range(1, N):
            v = arr[i-1]                
            counter[v] -= 1            
            if v>1-i:
                points += 1
            counter[v-N] += 1            
            points -= counter[1-i]            
            if points>max_points:
                ret = i
                max_points = points        
        return ret
        
if __name__ == '__main__':
    sol = Solution()
    A = [2,3,1,4,0]
    assert sol.bestRotationNoTLE(A) == 3