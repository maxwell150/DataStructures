"""
traversing the binary tree using inorder traversal that is:
	traverse the left subtree recursively
	traverse the current node
	traverse the right subtree recursively inorder
"""
from simple_binary_tree import BinaryTree
from binary_tree_input import input_data

sample_input = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

node = input_data(sample_input)

def inorder_traversal(node):

    if node is None:
        return []
    return (inorder_traversal(node.left) + [node.key] + inorder_traversal(node.right))

# print(inorder_traversal(node))
# output = [1, 3, 2, 3, 4, 5, 6, 7, 8]
