"""155. Min Stack
Medium
Topics
premium lock icon
Companies
Hint
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int value) pushes the element value onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
"""

class Node:
    """
    Represents a node in the doubly-linked list.
    
    Attributes:
        val (int): The value stored in the node.
        minv (int): The minimum value in the stack up to this node.
        next (Node | None): Reference to the next node toward the tail.
        prev (Node | None): Reference to the previous node toward the head.
    """
    def __init__(self, val: int):
        self.val = val
        self.next, self.prev = None, None
        self.minv = val


class MinStack:
    """
    A LIFO Stack supporting push, pop, top, and getMin in O(1) time.
    """

    def __init__(self):
        """Initializes sentinel nodes and connects them."""
        self.left, self.right = Node(0), Node(0)
        self.right.prev, self.left.next = self.left, self.right

    def push(self, value: int) -> None:
        """
        Pushes an element onto the stack.
        
        Args:
            value (int): Element to be pushed.
        """
        node = Node(value)
        top_node = self.right.prev

        # Compute running minimum snapshot
        if top_node == self.left:
            node.minv = value
        else:
            node.minv = min(value, top_node.minv)

        # Splice node between current top node and right sentinel
        top_node.next = node
        node.prev = top_node
        node.next = self.right
        self.right.prev = node

    def pop(self) -> None:
        """
        Removes the top element from the stack.
        Guarded against stack underflow.
        """
        target = self.right.prev
        if target == self.left:
            return  # Stack is empty

        prev_node = target.prev
        prev_node.next = self.right
        self.right.prev = prev_node

        # Detach pointers to assist Python Garbage Collector
        target.prev = target.next = None

    def top(self) -> int:
        """
        Retrieves the top element value.
        
        Returns:
            int: Value of the top node.
        """
        return self.right.prev.val

    def getMin(self) -> int:
        """
        Retrieves the minimum element currently in the stack.
        
        Returns:
            int: Minimum value stored in top node's minv state.
        """
        return self.right.prev.minv


minStack = MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); # return -3
minStack.pop();
minStack.top();    # return 0
minStack.getMin(); # return -2
