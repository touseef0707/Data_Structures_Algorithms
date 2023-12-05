from Trees import User
from Treenode import TreeNode
from Trees1 import display_keys
touseef = User('rainyjoke', 'Touseef Ahmed', 'touseefahmed0707@gmail.com')
habiba = User('habiba.ak_5', 'Habiba Akter Nupur', 'habibaakter0707@gmail.com')
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')
users = [touseef, habiba, aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

"""
-----Storing Key-Value Pairs using BSTs-----
Recall that we need to store user objects with each key in our BST. 
Let's define new class BSTNode to represent the nodes of of our tree. 
Apart from having properties key, left and right, we'll also store a value 
and pointer to the parent node (for easier upward traversal).
"""

class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# tree = BSTNode(jadhesh.username, jadhesh)
# tree.left = BSTNode(biraj.username, biraj)
# tree.right = BSTNode(sonaksh.username, sonaksh)
# print(tree.left.key, tree.left.value, tree.right.key, tree.right.value)

"""Insertion into BST"""
def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node

tree1 = insert(None, jadhesh.username, jadhesh)
insert(tree1, touseef.username, touseef)
insert(tree1, habiba.username, habiba)
insert(tree1, biraj.username, biraj)
insert(tree1, hemanth.username, hemanth)
insert(tree1, jadhesh.username, jadhesh)
insert(tree1, siddhant.username, siddhant)
insert(tree1, sonaksh.username, sonaksh)
insert(tree1, vishal.username, vishal)

# display_keys(tree1)

""" some things are changed and not according to jovian
Skewed/unbalanced BSTs are problematic because the height of such trees often 
ceases to logarithmic compared to the number of nodes in the tree. For 
instance the above tree has 7 nodes and height 7.

The length of the path traversed by insert is equal to the height of the tree 
(in the worst case). It follows that if the tree is balanced, the time 
complexity of insertion is O(log N) otherwise it is O(N)."""

"""Finding Node"""

def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)

"""Updating a value"""

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value

"""List all"""

def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

"""Is a BST balanced?"""

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and \
               abs(height_l - height_r <= 1)
    height = 1 + max(height_l, height_r)
    return balanced, height

"""Create a balanced BST"""
# We can use a recursive strategy here, turning the middle element of the
# list into the root, and recursively creating left and right subtrees.

def make_balanced_BST(data, lo = 0 , hi = None, parent = None):
    if hi is None:
        hi = len(data) - 1

    if lo > hi:
        return None

    mid = (hi + lo)//2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_BST(data, lo, mid - 1, root)
    root.right = make_balanced_BST(data, mid+1, hi, root)

    return root

# data = [(user.username, user) for user in users]
# tree2 = make_balanced_BST(data)
# display_keys(tree2)

"""Balance an unbalanced BST"""

def balance_bst(node):
    return make_balanced_BST(list_all(node))

# tree3 = balance_bst(tree1)
# display_keys(tree3)

"""
## A Python-Friendly Treemap 

We are now ready to return to our original problem statement.

> **QUESTION 1**: As a senior backend engineer at Jovian, you are tasked 
    with developing a fast in-memory data structure to manage profile 
    information (username, name and email) for 100 million users. It should 
    allow the following operations to be performed efficiently:

> 1. **Insert** the profile information for a new user.
> 2. **Find** the profile information of a user, given their username.
> 3. **Update** the profile information of a user, given their username.
> 5. **List** all the users of the platform, sorted by username.
>
> You can assume that usernames are unique. 

We can create a generic class `TreeMap` which supports all the operations 
specified in the original problem statement in a python-friendly manner."""


class TreeMap():
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self, key):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return TreeNode.size(self.root)

    def display(self):
        return display_keys(self.root)

treemap = TreeMap()
treemap['biraj'] = biraj
treemap['hemanth'] = hemanth
treemap['siddhant'] = siddhant
treemap['vishal'] = vishal
treemap['aakash'] = aakash
treemap['jadhesh'] = jadhesh
treemap['sonaksh'] = sonaksh
treemap['habiba.ak_5'] = habiba
treemap['rainyjoke'] = touseef

print(treemap['aakash'], end='\n')
treemap.display()
print("")
for key, value in treemap:
    print(key, value)
print(list(treemap))
print("")
print("length:",len(treemap))
treemap['aakash'] = User(username='aakash', name='Aakash N S', email='aakashns@example.com')
print(treemap['aakash'])

