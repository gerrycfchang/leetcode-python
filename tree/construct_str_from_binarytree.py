# 606. Construct String from Binary Tree
# 
# You need to construct a string consists of parenthesis and integers from a binary tree with the preorder traversing way.
# 
# The null node needs to be represented by empty parenthesis pair "()". 
# And you need to omit all the empty parenthesis pairs 
# that don't affect the one-to-one mapping relationship between the string and the original binary tree.
# 
# Example 1:
# Input: Binary tree: [1,2,3,4]
#        1
#      /   \
#     2     3
#    /    
#   4     
# 
# Output: "1(2(4))(3)"
# 
# Explanation: Originallay it needs to be "1(2(4)())(3()())", 
# but you need to omit all the unnecessary empty parenthesis pairs. 
# And it will be "1(2(4))(3)".
# Example 2:
# Input: Binary tree: [1,2,3,null,4]
#        1
#      /   \
#     2     3
#      \  
#       4 
# 
# Output: "1(2()(4))(3)"
# 
# Explanation: Almost the same as the first example, 
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship 
# between the input and the output.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preorder(curr, res):
            if not curr: return
            tmp = str(curr.val)
            res.append(tmp)
            if (curr.left) or (not curr.left and curr.right) :
                res.append('(')
                preorder(curr.left, res)
                res.append(')')
            if curr.right:
                res.append('(')
                preorder(curr.right, res)
                res.append(')')               
        res = []
        preorder(t, res)
        return ''.join(res)        

if __name__ == '__main__':
    sol = Solution()
    """
    #     1
    #    / \
    #   2   3
    #  / 
    # 4   
    """
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    

    root.left = node1
    root.right = node2
    node1.left = node3
    res = sol.tree2str(root)
    assert ( res == '1(2(4))(3)')

    """
    #     1
    #    / \
    #   2   3
    #    \
    #     4   
    """
    root  = TreeNode(1)
    node1 = TreeNode(2)
    node2 = TreeNode(3)
    node3 = TreeNode(4)
    

    root.left = node1
    root.right = node2
    node1.right = node3
    res = sol.tree2str(root)
    assert ( res == '1(2()(4))(3)')