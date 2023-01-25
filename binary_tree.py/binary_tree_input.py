"""
This file involves creating a function that takes input and 
populates our binary tree instead of doing it manually like in the 
previous implementation
"""

from simple_binary_tree import BinaryTree

def input_data(data):
    """the data is provided in form of a tuple"""
    if isinstance(data, tuple) and len(data) == 3:
        rootNode = BinaryTree(data[1])
        rootNode.left = input_data(data[0])
        rootNode.right = input_data(data[2])

    elif data is None:
        rootNode = None

    else:
        rootNode = BinaryTree(data)

    return rootNode

sample_input = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
rootNode = input_data(sample_input)
print(rootNode.key) #2
print(rootNode.left.key) #3
print(rootNode.right.key) #5
