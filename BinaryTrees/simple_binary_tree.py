""" A simpe binary looks like the demonstration below where 3 is the root node, 4 the left child and 5
 the right child
 one you'll notice is that the left child is always < the right child
            3(node0)
           / \
          /   \
  (node1)4     5(node2)
Here is a simple implementation of the above binary tree
"""
class BinaryTree:
    """initialize constructor function that takes in a key"""
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

node0 = BinaryTree(3)
node1 = BinaryTree(4)
node2 = BinaryTree(5)

node0.left = node1
node0.right = node2

# print(f'{node0.key}\n{node0.left.key}\n{node0.right.key}\n')
# output 3 4 5
