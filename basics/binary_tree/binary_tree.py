class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "TreeNode(val={}, left={}, right={})".format(
            self.val,
            self.left.val if self.left else None,
            self.right.val if self.right else None
        )
