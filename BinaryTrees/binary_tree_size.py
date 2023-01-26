"""
a function to get the number of node in a binary tree
"""
from simple_binary_tree import BinaryTree
from binary_tree_input import input_data

sample_input = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
node = input_data(sample_input)

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
