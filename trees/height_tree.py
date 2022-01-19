class Node:
    """A node (of a binary search tree) has a left and right node reference,
    along with some data."""
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    @staticmethod
    def initialize(arr):
        """Does this work by insertion sort?  Is this a standardized algorithm
        for inserting/creating data in a binary search tree?

        TODO: Determine the algorithm for this method
        """
        tree = BinarySearchTree()
        n = len(arr)
        [tree.create(arr[i]) for i in range(n)]
        return tree

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def height_custom(root):
    """David Kilgore-implented solution."""
    def _height_recursive(node, count):
        if node.left:
            _height_recursive(node.left, count+1)

    count = 0
    _height_recursive(root, count)


def treeHeight(root):
    """
    level-order traversal
    https://www.geeksforgeeks.org/iterative-method-to-find-height-of-binary-tree/
    This counts the nodes - not edges - from root to furthest node.
    """
    # Base case
    if root is None:
        return 0
 
    # Create an empty queue for level order traversal
    q = []

    # Enqueue root and initialize height
    q.append(root)
    height = 0

    while(True):
        # nodeCountAtCurrentLevel(queue size) indicates number of nodes at
        # current level
        nodeCountAtCurrentLevel = len(q)
        if nodeCountAtCurrentLevel == 0 :
            return height
        else:
            height += 1

            # Dequeue all nodes of current level and Enqueue all nodes of next
            # level
            while(nodeCountAtCurrentLevel > 0):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                nodeCountAtCurrentLevel -= 1


def height(root):
    """Uses recursion to compute the height of a binary search tree; height is
    defined as the number of edges - not nodes - between the root and the
    deepest node.  The height of an empty tree is defined as -1.  When we
    return a value, we add +1 to it for the current node."""
    if root is None:
        return -1

    height_left = height(root.left)
    height_right = height(root.right)
 
    # ..
    return max(height_left, height_right) + 1

    # ..
    if height_left == -1 and height_right == -1:
        return height_left + 1
    elif height_left >= height_right:
        return height_left + 1
    else:
        return height_right + 1

def height2(node):
    """Some randomly-found implementation, similar to the 'height' function
    above."""
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)
 
        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1


def lca(root):
    pass


def lca_main(root, v1, v2):
    """I'm thinking of a method inloving recursion."""
    pass


if __name__ == '__main__':
    def _create_test_example_tree_1():
        arr = [3, 5, 2, 1, 4, 6, 7]
        tree = BinarySearchTree()
        n = len(arr)
        [tree.create(arr[i]) for i in range(n)]
        return tree

    tree = _create_test_example_tree_1()

    assert height(tree.root) == 3
    assert treeHeight(tree.root) == 4

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
    assert lca_main(tree, 1, 7) == 6
