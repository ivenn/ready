from basics.linked_list.linked_list import ListNode


def reverse(head):
    if not head or not head.next:
        return head

    new_head = head

    while head.next:
        cur = head.next
        head.next = head.next.next

        cur.next = new_head
        new_head = cur

    return new_head


def remove_by_value(head, val):
    if not head:
        return head

    dummy_head = ListNode("dummy")
    prev = dummy_head
    prev.next = head

    cur = head
    while cur:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next

    return dummy_head.next


def odd_even_list(head):
    if not head or not head.next:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next
        even.next = odd.next
        even = even.next

    odd.next = even_head

    return head


def is_palindrome(head):
    if not head or not head.next:
        return True

    ll_len = 0
    cur = head
    while cur:
        ll_len += 1
        cur = cur.next

    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow
    if ll_len % 2:
        slow = slow.next

    stack = []
    while slow:
        stack.append(slow.val)
        slow = slow.next

    cur = head
    while cur != mid:
        if cur.val != stack.pop():
            return False
        cur = cur.next

    return not stack


















