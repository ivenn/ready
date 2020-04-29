
def has_cycle(head):
    if not head or not head.next:
        return False

    fast = head.next.next
    slow = head.next

    while slow is not fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next

    return True


def get_cycle_start_index(head):
    if not head or not head.next:
        return None

    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            seeker = head
            while seeker != slow:
                seeker = seeker.next
                slow = slow.next
            return slow

    return None


def get_cycle_start_index_2(head):
    if not head or not head.next:
        return None

    cur = head
    nodes = set()

    while cur:
        if cur in nodes:
            return cur
        nodes.add(cur)
        cur = cur.next

    return None


def lists_intersection(head_a, head_b):
    cur_a = head_a
    cur_b = head_b
    len_a = 0
    len_b = 0

    while cur_a:
        len_a += 1
        cur_a = cur_a.next
    while cur_b:
        len_b += 1
        cur_b = cur_b.next

    cur_a = head_a
    cur_b = head_b
    for _ in range(abs(len_a - len_b)):
        if len_a > len_b:
            cur_a = cur_a.next
        else:
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next

    return cur_a


def get_nth_node_from_the_end(head, n):
    cur = head
    target = head

    for _ in range(n):
        if cur:
            cur = cur.next
        else:
            return None

    while cur:
        cur = cur.next
        target = target.next

    return target


def remove_nth_node_from_the_end(head, n):
    cur = head
    target = head

    for _ in range(n):
        if cur:
            cur = cur.next
        else:
            return None

    prev = None
    while cur:
        cur = cur.next
        prev = target
        target = target.next

    if not prev:
        return target.next
    else:
        prev.next = target.next
        return head



