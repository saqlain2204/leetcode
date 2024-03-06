'''
141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True
            
        return False
    
'''
Constraints:
The number of nodes in the list is in the range [0, 10^4].
-10^5 <= Node.val <= 10^5
pos is -1 or a valid index in the linked list.

Test cases:
head = [3,2,0,-4], pos = 1
Answer: True

head = [1,2], pos = 0
Answer: True

head = [1], pos = -1
Answer: False
'''
input = ListNode(3)
input.next = ListNode(2)
input.next.next = ListNode(0)
input.next.next.next = ListNode(-4)
input.next.next.next.next = input.next
print(Solution().hasCycle(input)) # True

input = ListNode(1)
input.next = ListNode(2)
input.next.next = input
print(Solution().hasCycle(input)) # True

input = ListNode(1)
print(Solution().hasCycle(input)) # False