import linked_list
from linked_list import *


def add_two_numbers(l1, l2) -> ListNode:
    def create_numb(head: ListNode) -> int:
        # creating simple list from linked list
        numb_list = linked_list.create_simple_list(head=head)
        numb_list.reverse()
        # creating numb from digits from simple list
        s = ""
        for digit in numb_list:
            s += str(digit)
        numb = int(s)
        return numb

    def from_numb_to_list(numb: int) -> List:
        out_list = []
        while numb != 0:
            out_list.append(numb % 10)
            numb = numb // 10
        return out_list

    numb1 = create_numb(l1)
    numb2 = create_numb(l2)
    s = numb1 + numb2
    a = from_numb_to_list(s)
    # creating linked list from simple list
    head = linked_list.create_linked_list(simple_list=a)
    return head


my_l1 = linked_list.create_linked_list([2, 4, 3])
my_l2 = linked_list.create_linked_list([5, 6, 4])
output_linked_list = add_two_numbers(my_l1, my_l2)
linked_list.print_linked_list(output_linked_list)

