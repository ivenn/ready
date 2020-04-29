import unittest
from basics.linked_list.linked_list import ListNode
from basics.linked_list.two_pointers_problems import has_cycle

class TestLinkedListProblems(unittest.TestCase):

    def test_cycle(self):
        node1 = ListNode(1)
        node2 = ListNode(2)
        node3 = ListNode(3)
        node4 = ListNode(4)

        # no cycles
        node1.next = node2
        node2.next = node3
        node3.next = node4
        print(has_cycle(node1))
        assert has_cycle(node1) is False

        # one element cycled
        node1.next = node1
        assert has_cycle(node1) is True

        # big cycle
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node1
        assert has_cycle(node1) is True

        # small cycle
        node1.next = node2
        node2.next = node3
        node3.next = node4
        node4.next = node3
        assert has_cycle(node1) is True