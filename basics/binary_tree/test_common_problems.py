import unittest
from basics.binary_tree.binary_tree import TreeNode
from basics.binary_tree.common_problems import max_depth_bottom_up, max_depth_top_down
from basics.binary_tree.common_problems import serialize_tree, deserialize_tree, equal


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

    def test_max_depth_bottom_up(self):
        self.assertEqual(4, max_depth_bottom_up(self.binary_tree))

    def test_max_depth_top_down(self):
        self.assertEqual(4, max_depth_top_down(self.binary_tree))

    def test_equal(self):
        root1 = self.build_test_binary_tree()
        root2 = self.build_test_binary_tree()

        self.assertTrue(equal(root1, root2))

        root1.left.left = None
        self.assertFalse(equal(root1, root2))

    def test_serialize_deserialize(self):
        levels = serialize_tree(self.binary_tree)
        deserialized_root = deserialize_tree(levels)

        self.assertTrue(
            equal(deserialized_root, self.binary_tree)
        )