'''
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        position = length - n
        current = dummy

        for _ in range(position):
            current = current.next
        
        current.next = current.next.next
    
        return dummy.next
    
'''
Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Test Cases:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Input: head = [1], n = 1
Output: []

Input: head = [1,2], n = 1
Output: [1]
'''
input1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))  # [1, 2, 3, 4, 5]
input2 = ListNode(1)  # [1]
input3 = ListNode(1, ListNode(2))  # [1, 2]

sol = Solution()
print(sol.removeNthFromEnd(input1, 2))  # [1, 2, 3, 5]
print(sol.removeNthFromEnd(input2, 1))  # []
print(sol.removeNthFromEnd(input3, 1))  # [1]

