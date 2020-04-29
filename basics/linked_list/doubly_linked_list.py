class ListNode:

    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return "ListNode({val})".format(val=self.val)


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    @classmethod
    def from_list(cls, l):
        linked_list = cls()
        if not l:
            return linked_list

        dummy = ListNode("dummy")
        prev = dummy

        for val in l:
            cur = ListNode(val)
            cur.prev = prev
            prev.next = cur
            prev = cur

        linked_list.head = dummy.next
        return linked_list

    def to_list(self):
        res = []
        cur = self.head

        while cur:
            res.append(cur.val)
            cur = cur.next

        return res

    def get(self, index):
        cur = self.head
        while index and cur:
            index -= 1
            cur = cur.next

        return cur.val if cur else None

    def add_at_head(self, val):
        new_node = ListNode(val)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def add_at_tail(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return

        cur = self.head
        while cur.next:
            cur = cur.next

        cur.next = new_node
        new_node.prev = cur

    def add_at_index(self, val, index):
        if index < 0:
            raise ValueError("Index should be >= 0!")
        new_node = ListNode(val)
        if not self.head:
            if index == 0:
                self.head = new_node
                return
            else:
                raise ValueError("Index is larger than the list length!")

        cur = self.head
        index -= 1
        while cur.next and index:
            cur = cur.next
            index -= 1

        if index > 0:
            raise ValueError("Index is larger than the list length!")

        if cur.next:
            new_node.next = cur.next
            cur.next.prev = new_node
            cur.next = new_node
        else:
            cur.next = new_node
            new_node.prev = cur

    def delete_at_index(self, index):
        if index < 0:
            raise ValueError("Index should be >= 0!")
        if not self.head:
            raise ValueError("Index is larger than the list length!")
        if index == 0:
            self.head = self.head.next

        cur = self.head
        while cur.next and index:
            cur = cur.next
            index -= 1

        if index > 0:
            raise ValueError("Index is larger than the list length!")

        cur.prev.next = cur.next

    def __str__(self):
        l = self.to_list()
        if l:
            return "->".join([str(i) for i in l])
        else:
            return "<Empty>"

