# https://leetcode.com/problems/add-two-numbers/

"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummyHead = ListNode(0)
        tail = dummyHead

        while l1 is not None or l2 is not None or carry != 0:
            d1, d2 = 0, 0

            if l1 is not None:
                d1 = l1.val

            if l2 is not None:
                d2 = l2.val

            the_sum = d1 + d2 + carry
            digit = the_sum % 10
            carry = the_sum // 10

            # print("digit:", digit, "carry:", carry)
            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
