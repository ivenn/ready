import copy

from basics.binary_tree.binary_tree import TreeNode
from basics.binary_tree.traversals import level_order_traversal


def max_depth_bottom_up(root):
    if not root:
        return 0

    max_so_far = 0

    def max_depth(node, depth):
        nonlocal max_so_far
        if not node.left and not node.right:
            max_so_far = max(max_so_far, depth)
        else:
            if node.left:
                max_depth(node.left, 1 + depth)
            if node.right:
                max_depth(node.right, 1 + depth)

    max_depth(root, 1)

    return max_so_far


def max_depth_top_down(root):
    if not root:
        return 0
    return 1 + max(max_depth_top_down(root.left),
                   max_depth_top_down(root.right))


def is_symmetric(root):

    def is_mirror(left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        else:
            return (left.val == right.val and
                    is_mirror(left.right, right.left) and
                    is_mirror(left.left, right.right))

    return is_mirror(root, root)


def has_path_sum(root, target_sum):

    def path_sum(node, sum_left):
        if not node:
            return False
        if not node.left and not node.right and node.val == sum_left:
            return True
        return (path_sum(node.left, sum_left-node.val) or
                path_sum(node.right, sum_left - node.val))

    return path_sum(root, target_sum)


def build_tree_from_inorder_preorder(inorder, preorder):
    if not inorder or not preorder:
        return None
    inorder_map = {val: i for i, val in enumerate(inorder)}

    def helper(lo, hi):
        if lo > hi:
            return None
        node = TreeNode(preorder.pop(0))
        mid = inorder_map[node.val]
        node.left = helper(lo, mid - 1)
        node.right = helper(mid + 1, hi)
        return node

    return helper(0, len(inorder) - 1)


def build_tree_from_inorder_postorder(inorder, postorder):
    if not inorder or not postorder:
        return None
    inorder_map = {val: i for i, val in enumerate(inorder)}

    def helper(lo, hi):
        if lo > hi:
            return None
        node = TreeNode(postorder.pop())
        mid = inorder_map[node.val]
        node.right = helper(mid+1, hi)
        node.left = helper(lo, mid-1)
        return node

    return helper(0, len(inorder)-1)


def next_right_pointer(root):
    """
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
            self.next = None
    """
    levels = []
    to_do = [root]

    while to_do:
        cur_level = []
        next_to_do = []
        for n in to_do:
            if n is not None:
                cur_level.append(n)
                next_to_do += [n.left, n.right]
        if cur_level:
            levels.append(cur_level)
        to_do = next_to_do

    for level in levels[1:]:
        level.append(None)
        for i in range(1, len(level)):
            level[i-1].next = level[i]

    return root


def lowest_common_ancestor(root, p, q):
    answer = None

    def recurse_tree(node):
        nonlocal answer
        if not node:
            return False

        left = recurse_tree(node.left)
        right = recurse_tree(node.right)

        mid = node == p or node == q
        if mid + left + right >= 2:
            answer = node

        return mid or left or right

    recurse_tree(root)

    return answer


def lowest_common_ancestor_2(root, p, q):
    if root == p or root == q:
        return root

    left = right = None

    if root.left:
        left = lowest_common_ancestor_2(root.left, p, q)
    if root.right:
        right = lowest_common_ancestor_2(root.right, p, q)

    if left and right:
        return root
    else:
        return left or right


def lowest_common_ancestor_3(root, p, q):
    stack = [root]
    parents = {root: None}

    while p not in parents or q not in parents:
        node = stack.pop()
        if node.left:
            parents[node.left] = node
            stack.append(node.left)
        if node.right:
            parents[node.right] = node
            stack.append(node.right)

    ancestors = set()
    while p:
        ancestors.add(p)
        p = parents[p]

    while q not in ancestors:
        q = parents[q]

    return q


def serialize_tree(root):
    levels = level_order_traversal(root)
    return levels


def deserialize_tree(serialized):
    if not serialized:
        return None
    levels = copy.deepcopy(serialized)
    root = TreeNode(levels.pop(0)[0])
    nodes = [root]
    while levels:
        level = levels.pop(0)
        next_nodes = []
        for i, node in enumerate(nodes):
            if node:
                node.left = TreeNode(level[2*i]) if level[2*i] else None
                node.right = TreeNode(level[2*i+1]) if level[2*i+1] else None
                next_nodes += [node.left, node.right]
            else:
                next_nodes += [None, None]
        nodes = next_nodes

    return root


def equal(root1, root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    return (root1.val == root2.val and
            equal(root1.left, root2.left) and
            equal(root1.right, root2.right))






