# 113. Path Sum II
# 
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
# 
# For example:
# Given the below binary tree and sum = 22,
#               5
#              / \
#             4   8
#            /   / \
#           11  13  4
#          /  \    / \
#         7    2  5   1
# return
# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        self.inorder(root, [], sum, res)
        return res
    
    def inorder(self, node, path, target, res):
        if not node: return
        self.inorder(node.left, path+[node.val], target, res)
        if not node.left and not node.right and (sum(path) + node.val) == target:
            path += [node.val]
            res.append(path)
        self.inorder(node.right, path+[node.val], target, res)
        

if __name__ == '__main__':
    sol = Solution()
    #               5
    #              / \
    #             4   8
    #            /   / \
    #           11  13  4
    #          /  \    / \
    #         7    2  5   1
    # return
    # [
    #    [5,4,11,2],
    #    [5,8,4,5]
    # ]

    root  = TreeNode(5)
    node1 = TreeNode(4)
    node2 = TreeNode(8)
    node3 = TreeNode(11)
    node4 = TreeNode(13)
    node5 = TreeNode(4)
    node6 = TreeNode(7)
    node7 = TreeNode(2)
    node8 = TreeNode(5)
    node9 = TreeNode(1)

    root.left = node1
    root.right = node2
    node1.left = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node5.left = node8
    node5.right = node9

    exp = [
            [5,4,11,2],
            [5,8,4,5]
        ]
    assert sol.pathSum(root, 22) == exp