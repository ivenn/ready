class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

    def __repr__(self):
        return "ListNode(%s)" % self.val


def build_list(l):

    if not l:
        return None

    head = ListNode(l[0])
    cur = head

    for val in l[1:]:
        cur.next = ListNode(val)
        cur = cur.next

    return head


def print_list(head):

    cur = head
    res = []

    while cur:
        res.append(cur.val)
        cur = cur.next
    if res:
        print('->'.join([str(i) for i in res]))
    else:
        print('<Empty>')


def delete_node_by_val(head, val):

    if not head:
        return None

    dummy = ListNode(-1)
    dummy.next = head
    prev = dummy
    cur = head

    while cur:
        if cur.val == val:
            prev.next = cur.next
            cur.next = None
            break
        prev = cur
        cur = cur.next

    return dummy.next


def delete_node_by_index(head, index):

    if not head:
        return None

    dummy = ListNode(-1)
    dummy.next = head
    cur = head
    prev = dummy
    i = 1

    while cur:
        if i == index:
            prev.next = cur.next
            cur.next = None
            break
        prev = cur
        cur = cur.next
        i += 1

    return dummy.next


def size_iter(head):
    if not head:
        return 0

    cur = head
    size = 0

    while cur:
        size += 1
        cur = cur.next

    return size


def size_recur(head):
    if not head:
        return 0
    else:
        return 1 + size_recur(head.next)


def middle(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr
