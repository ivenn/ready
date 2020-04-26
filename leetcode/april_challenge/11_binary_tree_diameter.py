# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_nodes = 0

        def process_node(node):
            if not node:
                return 0

            left = process_node(node.left)
            right = process_node(node.right)
            d = 1 + left + right

            if d > self.max_nodes:
                self.max_nodes = d

            return 1 + max(left, right)

        process_node(root)

        return max(0, self.max_nodes - 1)
