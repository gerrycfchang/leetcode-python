# 508. Most Frequent Subtree Sum
# 
# Given the root of a tree, you are asked to find the most frequent subtree sum. 
# The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node 
# (including the node itself). 
# So what is the most frequent subtree sum value? 
# If there is a tie, return all the values with the highest frequency in any order.
# 
# Examples 1
# Input:
# 
#   5
#  /  \
# 2   -3
# return [2, -3, 4], since all the values happen only once, return all of them in any order.
# Examples 2
# Input:
# 
#   5
#  /  \
# 2   -5
# return [2], since 2 happens twice, however -5 only occur once.


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# from collections import Counter()
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        def inorder(node, dic):
            if not node: return 0
            if not node.left and not node.right:
                dic[node.val] = dic.get(node.val,0) + 1
                return node.val
            leftVal =  inorder(node.left, dic)
            rightVal = inorder(node.right,dic)
            total = leftVal + rightVal + node.val
            dic[total] = dic.get(total,0) + 1
            return total
        dic, res = {}, []
        inorder(root, dic)
        _, val = max(dic.items(), key=lambda x:x[1])
        for k, v in dic.items():
            if v == val:
                res.append(k)
        return res


if __name__ == '__main__':
    sol = Solution()
    
    assert sol.findFrequentTreeSum(None) == []
    #    5
    #   / \
    #  2   -3
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(-3)
    root.left = node1
    root.right = node2
    assert sol.findFrequentTreeSum(root) == [2, -3, 4]

    #    5
    #   / \
    #  2   -5
    root = TreeNode(5)
    node1 = TreeNode(2)
    node2 = TreeNode(-5)
    root.left = node1
    root.right = node2
    assert sol.findFrequentTreeSum(root) == [2]

    #    1
    #   / 
    #  1   
    root = TreeNode(1)
    node1 = TreeNode(1)
    root.left = node1
    assert sol.findFrequentTreeSum(root) == [1, 2]