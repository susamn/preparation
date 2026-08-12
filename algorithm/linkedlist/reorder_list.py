"""
143. Reorder List

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
 

Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
from typing import Optional

# Definition for singly-linked list.
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
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: find the middle using slow/fast pointers.
        # When fast reaches the end, slow is at the middle
        # (for even length, slow lands on the first node of the second half's
        #  "left-biased" split point — verified below).
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: split into two halves. second half starts right after slow.
        second = slow.next
        slow.next = None  # cut the first half

        # Step 3: reverse the second half.
        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        second = prev  # prev is now the head of the reversed second half

        # Step 4: merge the two halves alternately.
        first = head
        while second:
            # The sequencing here matters, dont do the last two lines before
            # forwarding first and next
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

sol = Solution()

# [1,2,3,4] -> [1,4,2,3]
n4 = ListNode(4)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)
sol.reorderList(n1)
print(f"[1,2,3,4]   -> {list_to_array(n1)}  (expected [1, 4, 2, 3])")

# [1,2,3,4,5] -> [1,5,2,4,3]
m5 = ListNode(5)
m4 = ListNode(4, m5)
m3 = ListNode(3, m4)
m2 = ListNode(2, m3)
m1 = ListNode(1, m2)
sol.reorderList(m1)
print(f"[1,2,3,4,5] -> {list_to_array(m1)}  (expected [1, 5, 2, 4, 3])")