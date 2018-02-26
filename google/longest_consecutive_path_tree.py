class TreeNode(object):
    def __init__(self, val):
        self.value = val
        self.childs = []

class Solution(object):
    def longestConsecutivePath(self, root):
        maxNum = [0]
        self.dfs(root, root.value, 1, maxNum)
        return maxNum[0]

    def dfs(self, node, value, out, maxNum):
        if node.value == value + 1:
            out += 1
        else:
            out = 1
        maxNum[0] = max(out, maxNum[0])
        for i in range(len(node.childs)):
            self.dfs(node.childs[i], node.value, out, maxNum)

if __name__ == '__main__':
    root   = TreeNode(2)
    node11 = TreeNode(5)
    node12 = TreeNode(7)
    node13 = TreeNode(3)
    node14 = TreeNode(6)

    node21 = TreeNode(6)
    node22 = TreeNode(3)
    node23 = TreeNode(2)
    node24 = TreeNode(4)
    node25 = TreeNode(5)
    node26 = TreeNode(8)

    node31 = TreeNode(3)

    node23.childs.append(node31)
    node11.childs.append(node21)
    node11.childs.append(node22)
    node12.childs.append(node23)
    node13.childs.append(node24)
    node14.childs.append(node25)
    node14.childs.append(node26)

    root.childs.append(node11)
    root.childs.append(node12)
    root.childs.append(node13)
    root.childs.append(node14)

    sol = Solution()
    assert sol.longestConsecutivePath(root) == 3



