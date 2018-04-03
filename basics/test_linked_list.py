from linked_list import *


def test_delete_node_by_val():
    l1 = build_list([1, ])
    l2 = build_list([1, 2])
    l3 = build_list([1, 2, 3, 4, 5])

    print_list(delete_node_by_val(l1, 0))
    print_list(delete_node_by_val(l1, 1))
    print_list(delete_node_by_val(l2, 0))
    print_list(delete_node_by_val(l2, 1))
    print_list(delete_node_by_val(l2, 2))
    print_list(delete_node_by_val(l3, 0))
    print_list(delete_node_by_val(l3, 3))


def test_delete_node_by_index():
    delete_node_by_index
    l1 = build_list([1, ])
    l2 = build_list([1, 2])
    l3 = build_list([1, 2, 3, 4, 5])

    print_list(delete_node_by_index(l1, 0))
    print_list(delete_node_by_index(l1, 1))
    print_list(delete_node_by_index(l2, 0))
    print_list(delete_node_by_index(l2, 1))
    print_list(delete_node_by_index(l2, 1))
    print_list(delete_node_by_index(l3, 0))
    print_list(delete_node_by_index(l3, 3))


def test_size():
    l1 = build_list([1, ])
    l2 = build_list([1, 2])
    l3 = build_list([1, 2, 3, 4, 5])

    print(size_iter(l1))
    print(size_iter(l2))
    print(size_iter(l3))
    print(size_recur(l1))
    print(size_recur(l2))
    print(size_recur(l3))


def test_middle():
    l1 = build_list([1, ])
    l2 = build_list([1, 2])
    l3 = build_list([1, 2, 3, 4, 5])

    print(middle(l1))        
    print(middle(l2))    
    print(middle(l3))


if __name__ == "__main__":
    test_delete_node_by_val()
    print '-'*50
    test_delete_node_by_index()
    print '-'*50
    test_size()
    print '-'*50
    test_middle()