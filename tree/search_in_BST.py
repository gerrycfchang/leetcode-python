# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.seqlist = []

    def __str__(self):
        self.inorder(self)
        return ' '.join(str(x) for x in self.seqlist)

    def inorder(self, curr):
        if not curr: return
        self.inorder(curr.left)
        self.seqlist.append(curr.val)
        self.inorder(curr.right)

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        
        Solution.ret = [0]
        def dfs(node, val):
            if not node: return
            dfs(node.left, val)
            if node.val == val:
                Solution.ret[0] = node
            dfs(node.right, val)
        dfs(root, val)
        return Solution.ret[0] if Solution.ret[0] else None


if __name__ == '__main__':
    obj = Solution()

    #      4
    #     / \
    #    2   7
    #   / \
    #  1   3
    root  = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(7)
    node3 = TreeNode(1)
    node4 = TreeNode(3)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4

    res   = TreeNode(2)
    lnode = TreeNode(1)
    rnode = TreeNode(3)
    res.left = lnode
    res.right = rnode

    output = obj.searchBST(root, 2)
    assert str(res) == str(output)