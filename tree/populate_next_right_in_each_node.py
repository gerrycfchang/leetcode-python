# 116. Populating Next Right Pointers in Each Node
# 
# Populate each next pointer to point to its next right node. 
# If there is no next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# Note:
# 
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra space for this problem.
# You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
# Example:
# 
# Given the following perfect binary tree,
# 
#      1
#    /  \
#   2    3
#  / \  / \
# 4  5  6  7
# After calling your function, the tree should look like:
# 
#      1 -> NULL
#    /  \
#   2 -> 3 -> NULL
#  / \  / \
# 4->5->6->7 -> NULL


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

from collections import defaultdict
class Solution:
    # @param root, a tree link node
    # @return nothing
    
    def connect(self, root):
        def inorder(node, level, dic):
            if not node: return
            inorder(node.left, level+1, dic)
            if len(dic[level]) > 0:
                dic[level][-1].next = node
            dic[level].append(node)
            inorder(node.right, level+1, dic)
        dic = defaultdict(list)
        inorder(root, 1, dic)

if __name__ == '__main__':
    sol = Solution()
    """
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    """
    root  = TreeLinkNode(3)
    node1 = TreeLinkNode(9)
    node2 = TreeLinkNode(20)
    node3 = TreeLinkNode(15)
    node4 = TreeLinkNode(7)

    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4
    sol.connect(root)
        
        