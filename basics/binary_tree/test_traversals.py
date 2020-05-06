import unittest
from basics.binary_tree.binary_tree import TreeNode
from basics.binary_tree.traversals import preorder_traversal, preorder_traversal_iter
from basics.binary_tree.traversals import inorder_traversal, inorder_traversal_iter
from basics.binary_tree.traversals import postorder_traversal, postorder_traversal_iter
from basics.binary_tree.traversals import level_order_traversal


class TestTraversals(unittest.TestCase):

    def build_test_binary_tree(self):
        """
        Test tree:
                    F
                  |  \
                 B    G
                | \  |  \
               A   D     I
                  | \   |
                  C E   H
        """
        node35 = TreeNode("H")
        node34 = TreeNode("E")
        node33 = TreeNode("C")
        node24 = TreeNode("I", left=node35)
        node22 = TreeNode("D", left=node33, right=node34)
        node21 = TreeNode("A")
        node12 = TreeNode("G", right=node24)
        node11 = TreeNode("B", left=node21, right=node22)
        root = TreeNode("F", left=node11, right=node12)

        return root

    def setUp(self):
        self.binary_tree = self.build_test_binary_tree()

    def test_preorder_traversal(self):
        res = []
        node_action = lambda node: res.append(node.val)
        exp_res = list('FBADCEGIH')
        preorder_traversal(self.binary_tree, node_action)
        self.assertEqual(res, exp_res, "act: {} exp: {}".format(res, exp_res))
        res = []
        preorder_traversal_iter(self.binary_tree, node_action)
        self.assertEqual(res, exp_res, "act: {} exp: {}".format(res, exp_res))

    def test_inorder_traversal(self):
        res = []
        node_action = lambda node: res.append(node.val)
        exp_res = list('ABCDEFGHI')
        inorder_traversal(self.binary_tree, node_action)
        self.assertEqual(res, exp_res, "act: {} exp: {}".format(res, exp_res))
        res = []
        inorder_traversal_iter(self.binary_tree, node_action)
        self.assertEqual(res, exp_res, "act: {} exp: {}".format(res, exp_res))

    def test_postorder_traversal(self):
        res = []
        node_action = lambda node: res.append(node.val)
        exp_res = list('ACEDBHIGF')
        postorder_traversal(self.binary_tree, node_action)
        self.assertEqual(res, exp_res, "act: {} exp: {}".format(res, exp_res))
        res = []
        postorder_traversal_iter(self.binary_tree, node_action)
        self.assertEqual(res, exp_res, "act: {} exp: {}".format(res, exp_res))

    def test_level_order_traversal(self):
        self.assertEqual(level_order_traversal(self.binary_tree),
                         [["F"], ["B", "G"], ["A", "D", None, "I"],
                          [None, None, "C", "E", None, None, "H", None]]
                         )


if __name__ == '__main__':
    unittest.main()
