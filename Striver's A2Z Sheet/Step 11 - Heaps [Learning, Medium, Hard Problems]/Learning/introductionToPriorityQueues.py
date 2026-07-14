# mypy: disable-error-code="empty-body"
# QUESTION: Introduction to Priority Queues using Binary Heaps
# A priority queue is an abstract data type similar to a regular queue, but where
# each element has a "priority". Elements with higher priority are served before
# elements with lower priority. Binary heaps are the standard array-based
# implementation of a priority queue supporting insert and extract-top in
# logarithmic time and peek in constant time.
# The task (learning) is to understand and demonstrate the behaviour of a priority
# queue: push a set of elements, then repeatedly pop the highest-priority element.
#
# Example 1:
# Input: push [5, 1, 3, 8, 2] into a max-priority-queue, then pop all
# Output: [8, 5, 3, 2, 1]
# Explanation: A max-priority-queue always returns the current largest element.
#
# Constraints:
# 1 <= number of operations <= 10^5
# -10^9 <= value <= 10^9


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

from typing import List


class Solution:
    def priorityQueueDemo_brute(self, values: List[int]) -> List[int]:
        pass

    def priorityQueueDemo_better(self, values: List[int]) -> List[int]:
        pass

    def priorityQueueDemo_optimal(self, values: List[int]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.priorityQueueDemo_optimal([5, 1, 3, 8, 2]))
