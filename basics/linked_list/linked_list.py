class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "ListNode({val})".format(val=self.val)


class LinkedList:

    def __init__(self):
        self.head = None

    @classmethod
    def from_list(cls, l):
        linked_list = cls()
        if not l:
            return linked_list

        linked_list.head = ListNode(l[0])
        cur = linked_list.head

        for val in l[1:]:
            cur.next = ListNode(val)
            cur = cur.next

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
        new_head = ListNode(val)
        new_head.next = self.head
        self.head = new_head

    def add_at_tail(self, val):
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = ListNode(val)
        else:
            self.head = ListNode(val)

    def add_at_index(self, val, index):
        if index < 0:
            raise ValueError("Index should be >= 0!")
        if index == 0:
            return self.add_at_head(val)
        if not self.head:
            raise ValueError("Index is larger than the list length!")

        new_node = ListNode(val)
        cur = self.head
        index -= 1
        while index and cur.next:
            index -= 1
            cur = cur.next

        if index > 0:
            raise ValueError("Index is larger than the list length!")

        next_node = cur.next
        cur.next = new_node
        new_node.next = next_node

    def delete_at_index(self, index):
        if index < 0:
            raise ValueError("Index should be >= 0!")
        if not self.head:
            raise ValueError()

        dummy = ListNode(-1)
        dummy.next = self.head

        cur = self.head
        prev = dummy
        i = 0

        while cur:
            if i == index:
                prev.next = cur.next
                cur.next = None
                break
            prev = cur
            cur = cur.next
            i += 1
        else:
            raise ValueError()

        self.head = dummy.next

    def __str__(self):
        l = self.to_list()
        if l:
            return "->".join([str(i) for i in l])
        else:
            return "<Empty>"

