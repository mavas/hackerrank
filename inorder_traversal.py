"""
https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
"""


from common import Node, BinarySearchTree


"""
class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

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
"""


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)

This solution 100% works on HackerRank
"""
def inOrder(root):
    if root.left:
        inOrder(root.left)
    print(root.info, end=' ')
    if root.right:
        inOrder(root.right)

def inOrder2(root):
    """This returns a list, instead of just printing.  Not working yet."""
    o = []
    left_side = None
    right_side = None

    if root.left:
        left_side = inOrder(root.left)
    middle = root.info
    if root.right:
        right_side = inOrder(root.right)

    if left_side:
        o.append(left_side)
    o.append(middle)
    if right_side:
        o.append(right_side)

    return o


if __name__ == '__main__':
    def _create_test_example_tree(arr):
        return BinarySearchTree.initialize(arr)
    tree = _create_test_example_tree([1, 2, 5, 3, 6, 4])
    #assert inOrder2(tree.root) == [1, 2, 3, 4, 5, 6]
    print(inOrder2(tree.root))
