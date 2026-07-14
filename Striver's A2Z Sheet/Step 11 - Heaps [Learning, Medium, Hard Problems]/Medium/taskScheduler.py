# mypy: disable-error-code="empty-body"
# QUESTION: Task Scheduler
# Given a list of tasks (each represented by a character A-Z) and a non-negative
# integer n, each task takes one unit of time. In each unit the CPU could complete
# either one task or be idle. Two of the SAME task must be separated by at least n
# units of time. Return the least number of units of time the CPU needs to finish
# all tasks.
#
# Example 1:
# Input: tasks = ["A", "A", "A", "B", "B", "B"], n = 2
# Output: 8
# Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
#
# Example 2:
# Input: tasks = ["A", "C", "A", "B", "D", "B"], n = 1
# Output: 6
# Explanation: No idle time is needed; e.g. A -> B -> A -> B -> C -> D.
#
# Constraints:
# 1 <= tasks.length <= 10^4
# tasks[i] is an uppercase English letter
# 0 <= n <= 100


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
    def leastInterval_brute(self, tasks: List[str], n: int) -> int:
        pass

    def leastInterval_better(self, tasks: List[str], n: int) -> int:
        pass

    def leastInterval_optimal(self, tasks: List[str], n: int) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.leastInterval_optimal(["A", "A", "A", "B", "B", "B"], 2))
