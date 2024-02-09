'''
2816. Double a number represented as a linked list
https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/
'''
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        current = head
        while current != None:
            num = num * 10 + current.val
            current = current.next
        
        num *= 2

        digits = []
        if num == 0:
            digits = [0]
        while num > 0:
            digits.append(num%10)
            num //=10

        dummy = ListNode()
        curr = dummy
        for digit in reversed(digits):
            curr.next = ListNode(digit)
            curr = curr.next
        return dummy.next

'''
Constraints:
The number of nodes in the list is in the range [1, 104]
0 <= Node.val <= 9
The input is generated such that the list represents a number that does not have leading zeros, except the number 0 itself.

Test Cases:

Input: head = [1,8,9]
Output: [3,7,8]

Input: head = [9,9,9]
Output: [1,9,9,8]
'''