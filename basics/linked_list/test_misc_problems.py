import unittest
from basics.linked_list.linked_list import LinkedList
from basics.linked_list.misc_problems import merge_two_sorted_lists, add_two_numbers, rotate_right


class TestLinkedList(unittest.TestCase):

    def test_merge_two_sorted_lists(self):
        for l1, l2, exp_res in [([], [], []),
                                ([1], [], [1]),
                                ([], [1], [1]),
                                ([1, 3], [2, 4], [1, 2, 3, 4]),
                                ([2, 4], [1, 3], [1, 2, 3, 4])]:
            ll1 = LinkedList.from_list(l1)
            ll2 = LinkedList.from_list(l2)
            res_ll = LinkedList()
            res_ll.head = merge_two_sorted_lists(ll1.head, ll2.head)
            assert res_ll.to_list() == exp_res

    def test_add_two_numbers(self):
        for l1, l2, exp_res in [([2, 4, 3], [5, 6, 4], [7, 0, 8])]:
            ll1 = LinkedList.from_list(l1)
            ll2 = LinkedList.from_list(l2)
            res_ll = LinkedList()
            res_ll.head = add_two_numbers(ll1.head, ll2.head)
            assert res_ll.to_list() == exp_res

    def test_rotate_right(self):
        for l, k, exp_res in [([], 0, []),
                              ([1], 0, [1]),
                              ([1, 2], 1, [2, 1]),
                              ([1, 2, 3, 4, 5], 1, [5, 1, 2, 3, 4]),
                              ([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
                              ([1, 2, 3, 4, 5], 3, [3, 4, 5, 1, 2]),
                              ([1, 2, 3, 4, 5], 4, [2, 3, 4, 5, 1]),
                              ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5])]:
            ll = LinkedList.from_list(l)
            ll.head = rotate_right(ll.head, k)
            res = ll.to_list()
            self.assertEqual(res, exp_res, "params: {} act:{} exp:{}".format(
                (l, k), res, exp_res))

