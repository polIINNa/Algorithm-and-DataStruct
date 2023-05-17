import linked_list
from linked_list import *


my_linked_list = linked_list.create_linked_list([1, 2, 3, 4, 5, 6])


def swap_nodes(head: ListNode) -> ListNode:
    if head is not None and head.next_node is not None:
        #first swap to save new head
        cur = head
        nxt = cur.next_node
        cur.next_node = nxt.next_node
        nxt.next_node = cur
        head = nxt
        prev = cur
        cur = prev.next_node
        while cur is not None and cur.next_node is not None:
            nxt = cur.next_node
            cur.next_node = nxt.next_node
            nxt.next_node = cur
            prev.next_node = nxt
            prev = cur
            cur = prev.next_node
    return head


swapped_list = swap_nodes(my_linked_list)
linked_list.print_linked_list(swapped_list)


