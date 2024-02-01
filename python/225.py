'''
225. Implement Stack using Queues
https://leetcode.com/problems/implement-stack-using-queues/
'''
class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.insert(0, x)

    def pop(self) -> int:
        return self.stack.pop(0)

    def top(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
    
'''
Constraints:
1 <= x <= 9
At most 100 calls will be made to push, pop, top, and empty.
All the calls to pop and top are valid.

Test Cases:
Input: ["MyStack", "push", "push", "top", "pop", "empty"]
Output: [[], [1], [2], [], [], []]

Input: ["MyStack", "push", "push", "pop", "top", "empty"]
Output: [[], [1], [2], [], [], []]

Input: ["MyStack", "push", "push", "push", "pop", "pop", "pop", "empty"]
Output: [[], [1], [2], [3], [], [], [], []]
'''
