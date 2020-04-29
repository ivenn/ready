import unittest
from basics.linked_list.linked_list import LinkedList
from basics.linked_list.doubly_linked_list import DoublyLinkedList


class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.test_cls = DoublyLinkedList
        print("Using {}".format(self.test_cls.__name__))

    def test_from_to_list(self):
        for test_list in ([], [0], [0, 1, 2, 3]):
            assert self.test_cls.from_list(test_list).to_list() == test_list

    def test_get(self):
        ll = self.test_cls.from_list([0, 1, 2, 3])
        assert ll.get(-1) is None
        assert ll.get(0) == 0
        assert ll.get(2) == 2
        assert ll.get(3) == 3
        assert ll.get(10) is None

    def test_add_at_head(self):
        ll = self.test_cls()
        ll.add_at_head(0)
        assert ll.to_list() == [0]
        ll.add_at_head(1)
        assert ll.to_list() == [1, 0]
        ll.add_at_head(2)
        assert ll.to_list() == [2, 1, 0]

    def test_add_at_tail(self):
        ll = self.test_cls()
        ll.add_at_tail(0)
        assert ll.to_list() == [0]
        ll.add_at_tail(1)
        assert ll.to_list() == [0, 1]
        ll.add_at_tail(2)
        assert ll.to_list() == [0, 1, 2]

    def test_add_at_index(self):
        ll = self.test_cls()
        with self.assertRaises(ValueError):
            ll.add_at_index(0, -1)
        assert ll.head is None
        with self.assertRaises(ValueError):
            ll.add_at_index(0, 1)
        assert ll.head is None
        ll.add_at_index(0, 0)
        assert ll.to_list() == [0]

        with self.assertRaises(ValueError):
            ll.add_at_index(0, -1)
        assert ll.to_list() == [0]
        with self.assertRaises(ValueError):
            ll.add_at_index(0, 2)
        assert ll.to_list() == [0]
        ll.add_at_index(1, 1)
        assert ll.to_list() == [0, 1]
        with self.assertRaises(ValueError):
            ll.add_at_index(2, 3)
        ll.add_at_index(2, 2)
        assert ll.to_list() == [0, 1, 2]
        ll.add_at_index(22, 2)
        assert ll.to_list() == [0, 1, 22, 2]

    def test_delete_at_index(self):
        ll = self.test_cls()
        with self.assertRaises(ValueError):
            ll.delete_at_index(0)
        with self.assertRaises(ValueError):
            ll.delete_at_index(1)

        ll = self.test_cls.from_list([0, 1, 2])
        with self.assertRaises(ValueError):
            ll.delete_at_index(-1)
        assert ll.to_list() == [0, 1, 2]
        with self.assertRaises(ValueError):
            ll.delete_at_index(3)
        assert ll.to_list() == [0, 1, 2]
        ll.delete_at_index(0)
        assert ll.to_list() == [1, 2]
        ll.delete_at_index(1)
        assert ll.to_list() == [1]