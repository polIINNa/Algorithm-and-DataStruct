from typing import List


class ListNode:
    def __init__(self, val=None, next_node=None):
        self.val = val
        self.next_node = next_node


def create_linked_list(simple_list: List) -> ListNode:
    head = ListNode(simple_list[0])
    node = head
    for i in range(1, len(simple_list)):
        node.next_node = ListNode(simple_list[i])
        node = node.next_node
    return head


def print_linked_list(head: ListNode):
    node = head
    while node is not None:
        print(node.val)
        node = node.next_node


def create_simple_list(head: ListNode) -> List:
    node = head
    simple_list = []
    while node is not None:
        simple_list.append(node.val)
        node = node.next_node
    return simple_list


if __name__ == '__main__':
    my_linked_list = create_linked_list([1, 2, 3, 4])
    print_linked_list(my_linked_list)
    my_simple_list = create_simple_list(my_linked_list)
    print(type(my_simple_list), my_simple_list)

