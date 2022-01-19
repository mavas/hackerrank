from common import Node, BinarySearchTree


def lca(root, v1):
    """Is there anything that can be done about calling a driver function
    exactly 2 times, once per v1 and v2 (as opposed to an invokation that
    involves both)?"""

def lca_main(root, v1, v2):
    """
    I'm thinking of a method inloving recursion.

    Both v1 and v2 WILL indeed exist, so it's a matter of seeing if they are on
    the left or right.  If it's THIS node, somehow report that correctly maybe.

    Very proud of this one!  Thought it up completely and it passed all tests.
    January 18, 2022
    """
    if root is None:
        return None

    if root.info == v1 or root.info == v2:
        return root

    v1_location = lca_main(root.left, v1, v2)
    v2_location = lca_main(root.right, v1, v2)

    if v1_location and v2_location:
        return root.info
    elif v1_location and not v2_location:
        return v1_location
    elif not v1_location and v2_location:
        return v2_location


def _create_test_example_tree_2():
    arr = [4, 2, 3, 1, 7, 6]
    tree = BinarySearchTree()
    n = len(arr)
    [tree.create(arr[i]) for i in range(n)]
    return tree
def _create_test_example_tree_3():
    arr = [4, 2, 3, 1, 7, 6]
    return BinarySearchTree.initialize(arr)
tree = _create_test_example_tree_2()
#assert lca_main(tree.root, 1, 7) == 6
assert lca_main(tree.root, 1, 7) == 4
