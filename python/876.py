'''
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        ptr = head
        count = 0
        while ptr is not None:
            count += 1
            ptr = ptr.next

        mid = count//2
        # print(count, mid)
        new_ptr = head
        for i in range(0, mid):
            new_ptr = new_ptr.next
        
        return new_ptr 

'''
Constraints:
The number of nodes in the given list will be between 1 and 100.
0 <= Node.val <= 100

Test cases:
Input: [1,2,3,4,5]
Output: [3,4,5]

Input: [1,2,3,4,5,6]
Output: [4,5,6]

Input: [1]
Output: [1]
'''
input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)
input.next.next.next.next = ListNode(5)
print(Solution().middleNode(input).val) # 3

input = ListNode(1)
input.next = ListNode(2)
input.next.next = ListNode(3)
input.next.next.next = ListNode(4)
input.next.next.next.next = ListNode(5)
input.next.next.next.next.next = ListNode(6)
print(Solution().middleNode(input).val) # 4

input = ListNode(1)
print(Solution().middleNode(input).val) # 1



