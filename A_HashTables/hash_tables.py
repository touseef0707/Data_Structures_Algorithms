""""""
"""
In this assignment, you will recreate Python dictionaries from scratch using data 
structure called hash table.
Dictionaries in Python are implemented using a data structure called hash table. 
A hash table uses a list/array to store the key-value pairs, and uses a hashing 
function to determine the index for storing or retrieving the data associated with a 
given key.
-------------------------------------------------------------------------------
Your objective in this assignment is to implement a `HashTable` class which 
supports the following operations:

1. Insert: Insert a new key-value pair
2. Find: Find the value associated with a key
3. Update: Update the value associated with a key
5. List: List all the keys stored in the hash table

The `HashTable` class will have the following structure (note the function signatures):"""

class HashTable1:
    def insert(self, key, value):
        """Insert a new key-value pair"""
        pass

    def find(self, key):
        """Find the value associated with a key"""
        pass

    def update(self, key, value):
        """Change the value associated with a key"""
        pass

    def list_all(self):
        """List all the keys"""
        pass

"""
Data List
We'll build the HashTable class step-by-step. As a first step is to create a Python 
list which will hold all the key-value pairs. We'll start by creating a list of a 
fixed size.
"""
data_list = [None] * 5000

"""Hashing Function

A _hashing function_ is used to convert strings and other non-numeric data types 
into numbers, which can then be used as list indices. For instance, if a hashing 
function converts the string `"Aakash"` into the number `4`, then the key-value pair 
`('Aakash', '7878787878')` will be stored at the position `4` within the data list.

Here's a simple algorithm for hashing, which can convert strings into numeric list 
indices.
1. Iterate over the string, character by character
2. Convert each character to a number using Python's built-in `ord` function.
3. Add the numbers for each character to obtain the hash for the entire string 
4. Take the remainder of the result with the size of the data list


QUESTION 2: Complete the `get_index` function below which implements the hashing 
algorithm described above.
"""


def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0

    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number

        # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index

"""
#### Insert

To insert a key-value pair into a hash table, we can simply get the hash of the 
key, and store the pair at that index in the data list.
"""
# key, value = 'Aakash', '7878787878'
# idx = get_index(data_list, key)
# data_list[idx] = (key, value)
# data_list[get_index(data_list, 'Hemanth')] = ('Hemanth', '9595949494')
"""
#### Find

The retrieve the value associated with a pair, we can get the hash of the key 
and look up that index in the data list.
"""
# key, value = data_list[idx]
# print(key, value)
"""
#### List

To get the list of keys, we can use a simple."""
# keys = [kv[0] for kv in data_list if kv is not None]
# print(keys)


class BasicHashTable:
    def __init__(self, max_size):
        # 1. Create a list of size `max_size` with all values None
        self.data_list = [None] * max_size

    def insert(self, key, value):
    # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)

        # 2. Store the key-value pair at the right index
        self.data_list[idx] = key, value

    def find(self, key):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        # 2. Retrieve the data stored at the index
        kv = self.data_list[idx]

        # 3. Return the value if found, else return None
        if kv is None:
            raise IndexError('key not found')
        else:
            key, value = kv
            return value

    def update(self, key, value):
        # 1. Find the index for the key using get_index
        idx = get_index(self.data_list, key)
        # 2. Store the new key-value pair at the right index
        self.data_list[idx] = key, value

    def list_all_keys(self):
        # 1. Extract the key from each key-value pair
        return [kv[0] for kv in self.data_list if kv is not None]

    def list_all_pairs(self):
        # 1. Extract the key-value pairs
        return[kv for kv in self.data_list if kv is not None]

basic_table = BasicHashTable(max_size=1024)
# len(basic_table.data_list) == 1024
# Insert some values
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')

# # Find a value
# print(basic_table.find('Hemanth')=='8888888888')
# # Update a value
# basic_table.update('Aakash', '7777777777')
# # Check the updated value
# print(basic_table.find('Aakash') == '7777777777')
# # Get the list of keys
# print(basic_table.list_all_keys())
# # Get the list of key-value pairs
# print(basic_table.list_all_pairs())

"""
We'll define a function called `get_valid_index`, which starts searching the 
data list from the index determined by the hashing function `get_index` and 
returns the first index which is either empty or contains a key-value pair 
matching the given key.

**QUESTION 4: Complete the function `get_valid_index` below by following the 
instructions in the comments.**"""


def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    idx = get_index(data_list, key)
    while True:
        # Get the key-value pair stored at idx
        kv = data_list[idx]
        # If it is None, return the index
        if kv is None:
            return idx
        # If the stored key matches the given key, return the index
        k, v = kv
        if k == key:
            return idx
        # Move to the next index
        idx += 1
        # Go back to the start if you have reached the end of the array
        if idx == len(data_list):
            idx = 0



# Create an empty hash table
MAX_HASH_TABLE_SIZE = 4096
# data_list2 = [None] * MAX_HASH_TABLE_SIZE

# # New key 'listen' should return expected index
# print(get_valid_index(data_list2, 'listen') == 655)
#
# # Insert a key-value pair for the key 'listen'
# data_list2[get_index(data_list2, 'listen')] = ('listen', 99)
#
# # Colliding key 'silent' should return next index
# print(get_valid_index(data_list2, 'silent') == 656)

"""
### Hash Table with Linear Probing

We can now implement a hash table with linear probing.

**QUESTION 5: Complete the hash table (with linear probing) implementation below by 
following the instructions in the comments.**
"""


class ProbingHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def insert(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def find(self, key):
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        return None if kv is None else kv[1]

    def update(self, key, value):
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def list_all(self):
        return [kv[0] for kv in self.data_list if kv is not None]

# # Create a new hash table
# probing_table = ProbingHashTable()
# # Insert a value
# probing_table.insert('listen', 99)
# # Check the value
# print(probing_table.find('listen') == 99)
# # Insert a colliding key
# probing_table.insert('silent', 200)
# # Check the new and old keys
# print(probing_table.find('listen') == 99 and probing_table.find('silent') == 200)
# # Update a key
# probing_table.insert('listen', 101)
# # Check the value
# print(probing_table.find('listen') == 101)
# # list all
# print(probing_table.list_all())

MAX_HASH_TABLE_SIZE = 4096


class HashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size

    def get_valid_index(self, key):
        # Use Python's in-built `hash` function and implement linear probing
        idx = hash(key) % len(self.data_list)
        return idx

    def __getitem__(self, key):
        # Implement the logic for "find" here
        idx = get_valid_index(self.data_list, key)
        kv = self.data_list[idx]
        return None if kv is None else kv[1]

    def __setitem__(self, key, value):
        # Implement the logic for "insert/update" here
        idx = get_valid_index(self.data_list, key)
        self.data_list[idx] = key, value

    def __iter__(self):
        return (x for x in self.data_list if x is not None)

    def __len__(self):
        return len([x for x in self])

    def __repr__(self):
        from textwrap import indent
        pairs = [indent("{} : {}".format(repr(kv[0]), repr(kv[1])), '  ') for kv in self]
        return "{\n" + "{}".format(',\n'.join(pairs)) + "\n}"

    def __str__(self):
        return repr(self)

# Create a hash table
table = HashTable()

# Insert some key-value pairs
table['a'] = 1
table['b'] = 34

# Retrieve the inserted values
print(table['a'] == 1 and table['b'] == 34)

# Update a value
table['a'] = 99
# Check the updated value
print(table['a'] == 99)
# Get a list of key-value pairs
# print(list(table))
print(table)