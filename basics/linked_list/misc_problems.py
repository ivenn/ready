from basics.linked_list.linked_list import ListNode


def merge_two_sorted_lists(head_a, head_b):
    if not head_a or not head_b:
        return head_a if head_a else head_b

    dummy = ListNode("dummy")
    head = dummy
    cur_a = head_a
    cur_b = head_b
    cur = head
    while cur_a and cur_b:
        if cur_a.val < cur_b.val:
            new_node = cur_a
            cur_a = cur_a.next
        else:
            new_node = cur_b
            cur_b = cur_b.next

        cur.next = new_node
        cur = cur.next

    if cur_a:
        cur.next = cur_a
    elif cur_b:
        cur.next = cur_b

    return head.next


def add_two_numbers(head_a, head_b):
    a = []
    b = []

    cur_a = head_a
    while cur_a:
        a.append(str(cur_a.val))
        cur_a = cur_a.next

    cur_b = head_b
    while cur_b:
        b.append(str(cur_b.val))
        cur_b = cur_b.next

    res = str(int("".join(reversed(a))) + int("".join(reversed(b))))

    dummy = ListNode("dummy")
    cur = dummy
    for c in reversed(res):
        cur.next = ListNode(int(c))
        cur = cur.next

    return dummy.next


def deep_copy_linked_list_with_random_prt(head):
    """
    # Definition for a Node.
    class Node:
        def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
            self.val = int(x)
            self.next = next
            self.random = random
    """
    if not head:
        return None

    cur = head
    dummy = ListNode("dummy")
    copied_cur = dummy
    nodes = {id(None): None}
    while cur:
        copied_node = ListNode(cur.val)
        nodes[id(cur)] = copied_node
        copied_cur.next = copied_node
        copied_cur = copied_cur.next
        cur = cur.next

    copied_cur = dummy.next
    cur = head
    while copied_cur:
        copied_cur.random = nodes[id(cur.random)]
        copied_cur = copied_cur.next
        cur = cur.next

    return dummy.next


def rotate_right(head, k):
    """
    Input: 1->2->3->4->5->NULL, k = 2
    Output: 4->5->1->2->3->NULL
    Explanation:
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL
    """
    if not head or not head.next:
        return head

    ll_len = 0
    cur = head
    while cur:
        ll_len += 1
        cur = cur.next

    k = k % ll_len
    if not k:
        return head

    cur = head
    for _ in range(k):
        if not cur:
            raise ValueError()
        cur = cur.next

    rot_prt = head
    while cur.next:
        cur = cur.next
        rot_prt = rot_prt.next

    cur.next = head
    head = rot_prt.next
    rot_prt.next = None

    return head

