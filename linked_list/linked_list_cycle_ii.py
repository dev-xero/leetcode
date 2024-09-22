# https://leetcode.com/problems/linked-list-cycle-ii/

"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head

        # regular tortoise and hare algorithm
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast: break

        else: return None
        
        # head will now move to the intersection point
        while head != slow:
            head, slow = head.next, slow.next

        return head