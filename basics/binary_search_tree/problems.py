class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self._left_inorer(root)

    def _left_inorer(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        node = self.stack.pop()

        if node.right:
            self._left_inorer(node.right)
        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


def validate_bst(root):
    """
        2
       / \
      1   3

    Input: [2,1,3]
    Output: true
    """

    def helper(node, lower, upper):
        if not node:
            return True
        if lower >= node.val or node.val >= upper:
            return False
        if (not helper(node.left, lower, node.val) or
                not helper(node.right, node.val, upper)):
            return False
        return True

    return helper(root, float("-inf"), float("inf"))


def search_bst(root, val):
    if not root:
        return None
    if root.val == val:
        return root
    if root.val > val:
        return search_bst(root.left, val)
    if root.val < val:
        return search_bst(root.right, val)


def insert_bst(root, val):
    def insert(node, val):
        if val < node.val:
            if node.left:
                return insert(node.left, val)
            else:
                node.left = TreeNode(val)
        elif val > node.val:
            if node.right:
                return insert(node.right, val)
            else:
                node.right = TreeNode(val)

    if not root:
        return TreeNode(val)
    else:
        insert(root, val)

    return root


def delete_node(root, key):
    if not root:
        return
    if root.val > key:
        root.left = delete_node(root.left, key)
    elif root.val < key:
        root.right = delete_node(root.right, key)
    else:  # root.val == val
        if not root.right:
            return root.left
        if not root.left:
            return root.right

        # else node has both children
        tmp = root.right
        min_val = tmp.val
        while tmp.left:
            tmp = tmp.left
            min_val = tmp.val
        root.val = min_val
        root.right = delete_node(root.right, root.val)

    return root


def lowest_common_ancestor(root, p, q):
    if q > root.val and p > root.val:
        return lowest_common_ancestor(root.right, p, q)
    elif q < root.val and p < root.val:
        return lowest_common_ancestor(root.left, p, q)
    else:
        return root


def max_depth(root, cur_depth):
    if not root:
        return cur_depth
    if not root.left and not root.right:
        return 1 + cur_depth
    return max(max_depth(root.left, 1 + cur_depth),
               max_depth(root.right, 1 + cur_depth))


def is_balanced(root):
    if not root:
        return True

    max_left = max_depth(root.left, 0)
    max_right = max_depth(root.right, 0)

    return (abs(max_left - max_right) < 2 and
            is_balanced(root.left) and
            is_balanced(root.right))













