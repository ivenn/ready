import unittest

from basics.linked_list.linked_list import LinkedList
from basics.linked_list.classic_problems import reverse, odd_even_list, is_palindrome


class TestClassicProblems(unittest.TestCase):

    def test_reverse(self):
        ll = LinkedList.from_list([0, 1, 2, 3])
        reversed_ll = LinkedList()
        reversed_ll.head = reverse(ll.head)
        print(reversed_ll.to_list())
        assert reversed_ll.to_list() == [3, 2, 1, 0]

    def test_odd_even_list(self):
        ll = LinkedList.from_list([1, 2, 3, 4])
        res_ll = LinkedList()
        res_ll.head = odd_even_list(ll.head)
        print(res_ll)

    def test_is_palindrome(self):
        for source_list, exp_res in [([], True),
                           ([1], True),
                           ([1, 2, 1], True),
                           ([1, 2, 2, 1], True),
                           ([1, 1, 2, 1, 1], True),
                           ([1, 2, 2, 2], False),
                           ([1, 2, 2, 2, 2], False),
                           ([1, 2, 3], False)]:
            ll = LinkedList.from_list(source_list)
            assert exp_res == is_palindrome(ll.head)



