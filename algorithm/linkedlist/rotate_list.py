"""
61. Rotate List

Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Rotate the linked list to the right by k places.

        Approach:
          1. Walk the list once to find its length `n` and its tail node.
          2. Rotating by k is equivalent to rotating by k % n (rotating by
             exactly n brings the list back to its original order), so
             normalize k first. This also handles k = 0 or k being much
             larger than n without doing wasted full rotations.
          3. Connect tail.next = head, turning the list into a circle.
          4. The new head will be at position (n - k % n) from the old head.
             Walk (n - k) - 1 steps from the old head to find the new tail;
             its .next is the new head. Break the circle there.
        """
        if not head or not head.next or k == 0:
            return head

        # Step 1: find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1

        k %= n
        if k == 0:
            return head  # rotating by a multiple of n = no change

        # Step 2: make it circular
        tail.next = head

        # Step 3: find new tail = (n - k - 1) steps from old head
        steps_to_new_tail = n - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None  # break the circle

        return new_head





sol = Solution()

# [1,2,3,4,5], k = 2 -> [4,5,1,2,3]
n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
result = list_to_array(sol.rotateRight(n1, 2))
print(f"[1,2,3,4,5], k=2  -> {result}  (expected [4, 5, 1, 2, 3])")


