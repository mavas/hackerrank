"""
https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

Started working on this January 18, 2022
"""


class DoublyLinkedList:
    """A doubly-linked list."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    @staticmethod
    def create_doubly_linked_list_from_list(items):
        """Makes a DoublyLinkedList object from a Python list."""
        # Make the first node, using the first item at the head.
        first_node = DoublyLinkedList(items[0])
        items = items[1:]

        head = first_node
        current_node = first_node
        for item in items:
            new_node = DoublyLinkedList(item)
            current_node.next = new_node
            new_node.prev = current_node
            current_node = current_node.next

        return head


def get_data_list_of_doubly_linked_list(sll):
    """Converts a DoublyLinkedList object into a Python list."""
    rval = []
    while sll:
        rval.append(sll.data)
        sll = sll.next
    return rval


def print_items_of_doubly_linked_list(node):
    """Prints, in order, the items of a DoublyLinkedList object."""
    if node.prev = None:
        pass
    while node:
        if node.next:
            print(str(node.data) + " -> ", end='')
        else:
            print(node.data)
        node = node.next


def insert_node(llist, data):
    # Create the first node; or in other words, initialize the 'merged'
    # variable.  This all depends on whether or not the data is greater or less
    # than the head.
    if data < llist.data:
        merged = DoublyLinkedList(data)
        merged.next = llist
    elif data > llist.data:
        merged = llist

    # ..
    return merged


def main(head, data):
    """Driver function, used to test the above "merge_2_doubly_linked_lists"
    function."""
    head = DoublyLinkedList.create_doubly_linked_list_from_list(head)
    #print_items_of_doubly_linked_list(head)

    sll = insert_node(head, data)

    rval = get_data_list_of_doubly_linked_list(sll)
    return rval


assert main([1, 2, 3], 2) == [1, 2, 2, 3]
assert main([1, 3, 4, 10], 5) == [1, 3, 4, 5, 10]
