"""
traversing the binary tree using preorder traversal that is:
	traverse the current node
	traverse the left subtree recursiely preorder
	traverse the right subtree recursively preorder
"""
from binary_tree_input import input_data

sample_input = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

node = input_data(sample_input)

def preorder_traversal(node):

    if node is None:
        return []
    return ([node.key] + preorder_traversal(node.left) + preorder_traversal(node.right))

# print(preorder_traversal(node))
# output = [2, 3, 1, 5, 3, 4, 7, 6, 8]
