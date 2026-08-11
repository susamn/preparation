"""146. LRU Cache
Solved
Medium
Topics
premium lock icon
Companies
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 104
0 <= value <= 105
At most 2 * 105 calls will be made to get and put.
"""


from typing import List
class Node:
    """
    Doubly linked list node used by the LRU cache.

    Each node stores:
    - key: the cache key
    - val: the cached value
    - prev: previous node in the list
    - next: next node in the list
    """

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    """
    Least Recently Used (LRU) Cache.

    Uses:
    - A dictionary for O(1) key lookup.
    - A doubly linked list to maintain usage order.

    The linked list is maintained as:

        left <-> LRU <-> ... <-> MRU <-> right

    `left` and `right` are dummy/sentinel nodes.

    - left.next  -> least recently used node
    - right.prev -> most recently used node

    Time Complexity:
        get(): O(1) average
        put(): O(1) average

    Space Complexity:
        O(capacity)
    """

    def __init__(self, capacity: int):
        """
        Initialize the LRU cache.

        Args:
            capacity: Maximum number of items the cache can hold.
        """
        self.data = {}
        self.cap = capacity

        # Dummy nodes.
        # They make insertion/removal easier because we don't
        # need special cases for the beginning/end of the list.
        self.left = Node(0, 0)
        self.right = Node(0, 0)

        # Initially, the list is empty:
        #
        # left <-> right
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        """
        Insert a node at the most recently used (MRU) position.

        The node is inserted immediately before the right sentinel.

        Before:
            ... <-> prev <-> right

        After:
            ... <-> prev <-> node <-> right
        """
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def remove(self, node):
        """
        Remove a node from the doubly linked list.

        The dictionary is NOT modified here; this method only
        changes the linked-list connections.

        Before:
            prev <-> node <-> next

        After:
            prev <-> next
        """
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        """
        Return the value associated with key.

        If the key exists:
        1. Remove the node from its current position.
        2. Insert it at the MRU position.
        3. Return its value.

        If the key doesn't exist, return -1.

        Args:
            key: Key to look up.

        Returns:
            The cached value, or -1 if the key is not present.
        """
        if key in self.data:
            node = self.data[key]

            # Accessing a node makes it the most recently used.
            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a key-value pair.

        If the key already exists:
        - Update its value.
        - Move it to the MRU position.

        If the key doesn't exist:
        - Create a new node.
        - Add it to the dictionary.
        - Insert it at the MRU position.

        If the cache exceeds its capacity:
        - Remove the LRU node.
        - Remove that key from the dictionary.

        Args:
            key: Key to insert or update.
            value: Value associated with the key.
        """
        if key in self.data:
            node = self.data[key]

            # Update the existing value.
            node.val = value

            # Updating a key makes it the most recently used.
            self.remove(node)
            self.insert(node)

        else:
            # Create and store a new node.
            node = Node(key, value)
            self.data[key] = node

            # New nodes are the most recently used.
            self.insert(node)

        # If we've exceeded capacity, remove the LRU node.
        if len(self.data) > self.cap:
            lru = self.left.next

            # Remove from linked list.
            self.remove(lru)

            # Remove from dictionary.
            del self.data[lru.key]


lRUCache = LRUCache(2);
lRUCache.put(1, 1); # cache is {1=1}
lRUCache.put(2, 2); # cache is {1=1, 2=2}
lRUCache.get(1);    # return 1
lRUCache.put(3, 3); # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    # returns -1 (not found)
lRUCache.put(4, 4); # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    # return -1 (not found)
lRUCache.get(3);    # return 3
lRUCache.get(4);    # return 4
