"""
https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem
"""


from common import SinglyLinkedList


def get_data_list_of_singly_linked_list(sll):
    """Converts a SinglyLinkedList object into a Python list."""
    rval = []
    while sll:
        rval.append(sll.data)
        sll = sll.next
    return rval


def print_items_of_singly_linked_list(node):
    """Prints, in order, the items of a SinglyLinkedList object."""
    while node:
        if node.next:
            print(str(node.data) + " -> ", end='')
        else:
            print(node.data)
        node = node.next


def merge_2_singly_linked_lists(head1, head2):
    """
    Take 2 ordered singly linked lists and iteratively merge them into one
    ordered singly-linked list.

    The first step is to create and compute the first node of the result; also,
    we perminently remove one of the heads of the 2 lists.  Then, use a loop to
    loop through both heads and iteratively append to the result.

    merged -> points to the head of the result
    tail -> points to the tail of the result (so that appending to the result
        is possible)
    """
    # The problem statement states that either of the 2 lists may be NULL, so
    # handle this case here.
    if not head1 and not head2:
        return None
    elif not head1 and head2:
        return head2
    elif head1 and not head2:
        return head1

    # Compute the first node.  Or in other words, compute the initial value for
    # the 'merged' variable, and perminently modify either 'head1' or 'head2'.
    if head1.data > head2.data:
        merged = SinglyLinkedList(head2.data)
        head2 = head2.next
    elif head1.data < head2.data:
        merged = SinglyLinkedList(head1.data)
        head1 = head1.next
    elif head1.data == head2.data:
        merged = SinglyLinkedList(head1.data)  # head1 could be head2..
        head1 = head1.next                     # ..

    # Loop through the 2 lists.  On each iteration, we add a new node to the
    # output ('merged'), and remove a node from one of the 2 lists; we iterate
    # until both lists are empty.
    tail = merged
    while head1 != None or head2 != None:
        if head1 and head2:
            if head1.data > head2.data:
                new_node = SinglyLinkedList(head2.data)
                head2 = head2.next
            elif head1.data < head2.data:
                new_node = SinglyLinkedList(head1.data)
                head1 = head1.next
            else:
                new_node = SinglyLinkedList(head1.data)
                head1 = head1.next
        elif head1 and not head2:
            new_node = SinglyLinkedList(head1.data)
            head1 = head1.next
        elif not head1 and head2:
            new_node = SinglyLinkedList(head2.data)
            head2 = head2.next
        tail.next = new_node
        tail = new_node

    # ..
    return merged


def main(head1, head2):
    """Driver function, used to test the above "merge_2_singly_linked_lists"
    function."""
    head1 = SinglyLinkedList.create_singly_linked_list_from_list(head1)
    head2 = SinglyLinkedList.create_singly_linked_list_from_list(head2)
    #print_items_of_singly_linked_list(head1)

    sll = merge_2_singly_linked_lists(head1, head2)

    rval = get_data_list_of_singly_linked_list(sll)
    return rval


if __name__ == '__main__':
    assert main([1, 2, 3], [2]) == [1, 2, 2, 3]
    assert main([1, 3, 22], [2]) == [1, 2, 3, 22]
