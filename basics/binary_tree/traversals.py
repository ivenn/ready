
def preorder_traversal(root, node_action):
    if not root:
        return

    node_action(root)
    preorder_traversal(root.left, node_action)
    preorder_traversal(root.right, node_action)


def preorder_traversal_iter(root, node_action):
    stack = [root]

    while stack:
        node = stack.pop()
        node_action(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def inorder_traversal(root, node_action):
    if not root:
        return

    inorder_traversal(root.left, node_action)
    node_action(root)
    inorder_traversal(root.right, node_action)


def inorder_traversal_iter(root, node_action):
    stack = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        node_action(node)
        node = node.right


def postorder_traversal(root, node_action):
    if not root:
        return

    postorder_traversal(root.left, node_action)
    postorder_traversal(root.right, node_action)
    node_action(root)


def postorder_traversal_iter(root, node_action):
    stack = []
    node = root
    prev = None
    while node or stack:
        if node:
            stack.append(node)
            node = node.left
        else:
            node = stack[-1]
            if node.right is None or node.right == prev:
                node_action(node)
                stack.pop()
                prev = node
                node = None
            else:
                node = node.right


def level_order_traversal(root):
    levels = []
    to_do = [root]

    while to_do:
        cur_level = []
        next_to_do = []
        for n in to_do:
            if n is not None:
                cur_level.append(n.val)
                next_to_do += [n.left, n.right]
            else:
                cur_level.append(n)
                next_to_do += [None, None]
        if any(cur_level):
            levels.append(cur_level)
        else:
            break

        to_do = next_to_do

    return levels


def level_order_traversal2(root):
    levels = []
    to_do = [root]

    while to_do:
        cur_level = []
        next_to_do = []
        for n in to_do:
            if n is not None:
                cur_level.append(n.val)
                next_to_do += [n.left, n.right]
        if cur_level:
            levels.append(cur_level)
        to_do = next_to_do

    return levels



