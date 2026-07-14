# mypy: disable-error-code="empty-body"
# QUESTION: Job Sequencing Problem
# Given a set of N jobs where each job i has a deadline[i] and a profit[i]. Each job
# takes exactly 1 unit of time to complete, and only one job can be scheduled at a
# time. You earn a job's profit only if it is completed on or before its deadline.
# Maximize total profit and return the number of jobs done and the total profit.
#
# Example 1:
# Input: jobs = [(id=1, deadline=4, profit=20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
# Output: [2, 60]
# Explanation: Do job 3 (profit 40) at time 1 and job 1 (profit 20) by time 4:
# 2 jobs, total profit 60.
#
# Constraints:
# 1 <= N <= 10^5
# 1 <= deadline[i] <= N
# 1 <= profit[i] <= 500

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

from typing import List, Tuple


class Solution:
    def job_sequencing_brute(self, jobs: List[Tuple[int, int, int]]) -> List[int]:
        pass

    def job_sequencing_better(self, jobs: List[Tuple[int, int, int]]) -> List[int]:
        pass

    def job_sequencing_optimal(self, jobs: List[Tuple[int, int, int]]) -> List[int]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.job_sequencing_optimal([(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]))
