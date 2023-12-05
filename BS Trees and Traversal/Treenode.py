class TreeNode():
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def traverse_in_order(self):
        if self is None:
            return []
        return (TreeNode.traverse_in_order(self.left) +
                [self.key] +
                TreeNode.traverse_in_order(self.right))

    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space * level + '∅')
            return

        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space * level + str(self.key))
            return

        # If the node has children
        display_keys(self.right, space, level + 1)
        print(space * level + str(self.key))
        display_keys(self.left, space, level + 1)

    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

    """
    QUESTION 8: Write a function to check if a binary tree is a binary search tree (BST).

    QUESTION 9: Write a function to find the maximum key in a binary tree.

    QUESTION 10: Write a function to find the minimum key in a binary tree.
    """
    @staticmethod
    def remove_none(nums):
        return [x for x in nums if x is not None]

    @staticmethod
    def is_bst(node):
        if node is None:
            return True, None, None

        is_bst_l, min_l, max_l = is_bst(node.left)
        is_bst_r, min_r, max_r = is_bst(node.right)

        is_bst_node = (is_bst_l and is_bst_r
                       and (max_l is None or node.key > max_l)
                       and (min_r is None or node.key < min_r))

        min_key = min(remove_none([min_l, node.key, min_r]))
        max_key = max(remove_none([max_l, node.key, max_r]))

        return is_bst_node, min_key, max_key


