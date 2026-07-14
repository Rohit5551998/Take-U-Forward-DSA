# mypy: disable-error-code="empty-body"
# QUESTION: Shortest Job First (SJF) CPU Scheduling
# Given an array bt of the burst times of N processes that all arrive at time 0, apply
# the non-preemptive Shortest Job First scheduling policy (always run the process with
# the smallest burst time next). Return the average waiting time across all processes
# (rounded down / as required by the platform).
#
# Example 1:
# Input: bt = [4, 3, 7, 1, 2]
# Output: 4
# Explanation: Sorted burst times [1, 2, 3, 4, 7] give waiting times [0, 1, 3, 6, 10];
# average = 20 / 5 = 4.
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= bt[i] <= 10^9

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
    def shortest_job_first_brute(self, bt: List[int]) -> int:
        pass

    def shortest_job_first_better(self, bt: List[int]) -> int:
        pass

    def shortest_job_first_optimal(self, bt: List[int]) -> int:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.shortest_job_first_optimal([4, 3, 7, 1, 2]))
