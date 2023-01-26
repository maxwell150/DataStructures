"""
a function to get the height of BT that is length of the longest path from its root node to a leaf
"""
from simple_binary_tree import BinaryTree
from binary_tree_input import input_data

sample_input = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
node = input_data(sample_input)

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
