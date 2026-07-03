# QUESTION: Implement Min Stack
# Design a stack that supports the following operations in constant time: push, pop, top, and
# retrieving the minimum element.
# Implement the MinStack class:
# MinStack(): Initializes the stack object.
# void push(int val): Pushes the element val onto the stack.
# void pop(): Removes the element on the top of the stack.
# int top(): Gets the top element of the stack.
# int getMin(): Retrieves the minimum element in the stack.
#
# Examples:
# Example 1:
# Input:
# ["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"]
# [[], [-2], [0], [-3], [], [], [], []]
# Output: [null, null, null, null, -3, null, 0, -2]
# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();  // returns -3
# minStack.pop();
# minStack.top();     // returns 0
# minStack.getMin();  // returns -2
#
# Example 2:
# Input:
# ["MinStack", "push", "push", "getMin", "push", "pop", "getMin", "top"]
# [[], [5], [1], [], [3], [], [], []]
# Output: [null, null, null, 1, null, null, 1, 1]
# Explanation:
# MinStack minStack = new MinStack();
# minStack.push(5);
# minStack.push(1);
# minStack.getMin();  // returns 1
# minStack.push(3);
# minStack.pop();
# minStack.getMin();  // returns 1
# minStack.top();     // returns 1
#
# Constraints:
# -10^5 <= val <= 10^5
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 5*10^4 calls will be made to push, pop, top, and getMin.


"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""


class Solution:
    def implement_min_stack_brute(self) -> None:
        pass

    def implement_min_stack_better(self) -> None:
        pass

    def implement_min_stack_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
