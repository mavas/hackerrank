"""
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem
"""


from common import SinglyLinkedList


def findMergeNode(head1, head2):
    """
    https://github.com/rajgubrele/hackerrank_ds_linkedlist_Find-Merge-Point-of-Two-Lists_python

    Finally gave up and found this solution.  I felt stupid with the way this
    approached the problem, but I immediately understood it and reminded myself
    that there are a few different ways to solve the same problem.  This simply
    uses references: it collects all of the references in the first list and
    iterates through all of the references in the second list, and simply
    checks and see if any of the 2nd list matches any in the 1st list.
    """
    l = list()
    while head1 != None:
        l.append(head1)
        head1 = head1.next
    while head2 != None:
        if head2.next in l:
            return head2.next.data
        else:
            head2 = head2.next


def findMergeNode2(head1, head2):
    """My first strategy was to somehow wisely iterate through one or both of
    the lists, but I couldn't ultimately find anything.  The above solution is
    really kind of silly and disjoint from this one, but does indeed work and
    makes total sense.  Maybe this method is actually impossible, and a
    solution involves using a language's features."""
    while True:
        if head1.data == head2.data:
            if not head1.next and not head2.next:
                return head1.data
        head1 = head1.next
        head2 = head2.next
    return rval


def main(head1, head2):
    return findMergeNode(head1, head2)
    return findMergeNode2(head1, head2)


if __name__ == '__main__':
    """
     1
      \
       2--->3--->NULL
      /
     1
    """
    merge_index = 1
    list1_count = 3
    items1 = [1, 2, 3]
    list2_count = 1
    items2 = [1]

    a = SinglyLinkedList.create_singly_linked_list_from_list(items1)
    b = SinglyLinkedList.create_singly_linked_list_from_list(items2)

    ptr1 = a
    ptr2 = b
    for i in range(list1_count):
        if i < merge_index:
            ptr1 = ptr1.next
    for i in range(list2_count):
        if i != list2_count-1:
            ptr2 = ptr2.next
    ptr2.next = ptr1

    assert main(a, b) == 2

    """
    1--->2
	  \
	   3--->Null
	  /
	 1
    """
    merge_index = 2

    a = SinglyLinkedList.create_singly_linked_list_from_list(items1)
    b = SinglyLinkedList.create_singly_linked_list_from_list(items2)

    ptr1 = a
    ptr2 = b
    for i in range(list1_count):
        if i < merge_index:
            ptr1 = ptr1.next
    for i in range(list2_count):
        if i != list2_count-1:
            ptr2 = ptr2.next
    ptr2.next = ptr1

    assert main(a, b) == 3
