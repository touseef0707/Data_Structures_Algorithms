
from Trees import User

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

"""Manual node insertion"""
# node0 = TreeNode(3)
# node1 = TreeNode(4)
# node2 = TreeNode(5)
#
# node0.left = node1
# node0.right = node2

"""
It's a bit inconvenient to create a tree by manually connecting all the nodes. Let's 
write a helper function which can convert a tuple with the structure ( left_subtree, 
key, right_subtree) (where left_subtree and right_subtree are themselves tuples) into 
binary tree.

Here's an tuple representing the tree shown above:
"""
tree_tuple = ((1,3,None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

tree0 = parse_tuple(tree_tuple)
# print(tree0.key)

def tree_to_tuple(node):
    if node is None:
        tuple = None
    elif node.right == node.left == None:
        tuple = node.key
    else:
        tuple = (tree_to_tuple(node.left), node.key, tree_to_tuple(node.right))
    return tuple
# print(tree_to_tuple(tree0))

def display_keys(node, space='\t\t', level=0):
    # print(node.key if node else None, level)

    # If the node is empty
    if node is None:
        print(space * level + '∅')
        return

        # If the node is a leaf
    if node.left is None and node.right is None:
        print(space * level + str(node.key))
        return

    # If the node has children
    display_keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    display_keys(node.left, space, level + 1)

# display_keys(tree0)
"""Traversing a binary tree"""

"""Inorder Traversal"""

def traverse_in_order(node):
    if node is None:
        return []
    return(traverse_in_order(node.left) +
           [node.key] +
           traverse_in_order(node.right))

"""Preorder Traversal"""

def traverse_pre_order(node):
    if node is None:
        return []
    return ([node.key]+
            traverse_pre_order(node.left)+
            traverse_pre_order(node.right))

"""Postorder Traversal"""

def traverse_post_order(node):
    if node is None:
        return []
    return (traverse_pre_order(node.left)+
            traverse_pre_order(node.right)+
            [node.key])

# print(traverse_in_order(tree0))
# print(traverse_pre_order(tree0))
# print(traverse_post_order(tree0))

"""
-----HEIGHT AND SIZE OF ST-----
The height/depth of a binary tree is defined as the length of the longest path 
from its root node to a leaf. It can be computed recursively, as follows:
"""

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# print(tree_height(tree0))
"""
Here's a function to count the number of nodes in a binary tree.
"""
def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

# print(tree_size(tree0))

def tree_diameter(node):
    if node is None:
        return 0
    return 1+tree_height(node.left)+tree_height(node.right)

# print(tree_diameter(tree0))

"""
QUESTION 8: Write a function to check if a binary tree is a binary search tree (BST).

QUESTION 9: Write a function to find the maximum key in a binary tree.

QUESTION 10: Write a function to find the minimum key in a binary tree.
"""


def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    # print(node.key, min_key, max_key, is_bst_node)
    return is_bst_node, min_key, max_key

# print(is_bst(tree0))

