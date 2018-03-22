"""
783. Minimum Distance Between BST Nodes
refer to 
530. Minimum Absolute Difference in BST

Given a Binary Search Tree (BST) with the root node root, return the minimum difference 

between the values of any two different nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \    
    1   3  

while the minimum difference in this tree is 1, it occurs between node 1 and node 2, 
also between node 3 and node 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sortArray = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            sortArray.append(node.val)
            inorder(node.right)
        inorder(root)
        minDist = float('inf')
        for x in range (len(sortArray)-1, 0, -1):
            minDist = min(minDist, sortArray[x] - sortArray[x-1])
        return minDist

    def minDiffInBSTSol(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        Solution.minDist = float('inf')
        Solution.prev = None
        
        def inorder(node):
            if not node: return
            inorder(node.left)
            if Solution.prev:
                Solution.minDist = min (Solution.minDist, abs(node.val - Solution.prev.val))
            Solution.prev = node
            inorder(node.right)
        inorder(root)
        return Solution.minDist

if __name__ == '__main__':
    sol = Solution()

    ### Test case 1
    """
    Given binary tree [3,9,20,null,null,15,7],

           4
         /   \
        2      6
       / \    
      1   3  
    """
    root  = TreeNode(4)
    node1 = TreeNode(2)
    node2 = TreeNode(6)
    node3 = TreeNode(1)
    node4 = TreeNode(3)

    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    assert sol.minDiffInBST(root) == 1
    assert sol.minDiffInBSTSol(root) == 1


    """
    Given binary tree [3,9,20,null,null,15,7],

          90
         /   
        68      
       /  \    
      49   89 
        \
        52 
    """
    root  = TreeNode(90)
    node1 = TreeNode(68)
    node2 = TreeNode(49)
    node3 = TreeNode(89)
    node4 = TreeNode(52)

    root.left = node1
    node1.left = node2
    node1.right = node3
    node2.right = node4
    assert sol.minDiffInBST(root) == 1
    assert sol.minDiffInBSTSol(root) == 1
    