class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return "ListNode({})".format(self.val)


class Solution:

    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


def build_linked_list(l):
    head = ListNode(l.pop(0))
    cur = head
    while l:
        new_node = ListNode(l.pop(0))
        cur.next = new_node
        cur = new_node

    return head

def print_linked_list(l):
    cur = l
    res = []
    while cur:
        res.append(cur.val)
        cur = cur.next

    print("->".join([str(i) for i in res]))


def test():
    s = Solution()

    print(s.middleNode(build_linked_list([1,2,3,4,5,6])))

test()

