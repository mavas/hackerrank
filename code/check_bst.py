"""
https://www.hackerrank.com/challenges/ctci-is-binary-search-tree/problem

Not completed yet.
"""


from common import Node, BinarySearchTree


def check_bst(root):
    """Broken, still working on it."""
    if root is None:
        return None

    if root.left is None and root.right is None:
        return True

    left_node = check_bst(root.left)
    right_node = check_bst(root.right)
    print(left_node, left_node, root.info)

    if left_node and right_node:
        if isinstance(left_node, Node) and left_node.info < root.info:
            if isinstance(right_node, Node) and right_node.info > root.info:
                return True
        if left_node.info < root.info and right_node.info > root.info:
            return True
        else:
            return False
    elif left_node and not right_node:
        if left_node.info < root.info:
            return True
        return False
    elif not left_node and right_node:
        if isinstance(right_node, Node) and right_node.info > root.info:
            return True
        return right_node
    elif not left_node and not right_node:
        return True


if __name__ == '__main__':
    def _create_test_example_tree_4():
        arr = [1, 2, 4, 3, 5, 6, 7]
        return BinarySearchTree.initialize(arr)
    tree = _create_test_example_tree_4()
    print(check_bst(tree.root))
