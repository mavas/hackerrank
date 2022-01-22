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
