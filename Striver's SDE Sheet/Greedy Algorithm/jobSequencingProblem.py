# QUESTION: Job sequencing Problem
# Given a 2D array Jobs of size Nx3, where Jobs[i][0] represents JobID, Jobs[i][1] represents
# Deadline, and Jobs[i][2] represents the Profit associated with that job. Each job takes
# 1 unit of time to complete and only one job can be scheduled at a time.
# The profit associated with a job is earned only if it is completed by its deadline.
# Find the number of jobs done and the maximum profit.
#
# Examples:
# Example 1:
# Input: Jobs = [ [1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30] ]
# Output: 2 60
# Explanation: Job with JobID 3 can be performed at time t=1 giving a profit of 40.
# Job with JobID 1 can be performed at time t=2 giving a profit of 20.
# No more jobs can be scheduled, so total profit = 40 + 20 => 60.
# Total number of jobs completed is two (JobID 1, JobID 3). So the answer is 2 60.
#
# Example 2:
# Input: Jobs = [ [1, 2, 100], [2, 1, 19], [3, 2, 27], [4, 1, 25], [5, 1, 15] ]
# Output: 2 127
# Explanation: Job with JobID 1 can be performed at time t=1 giving a profit of 100.
# Job with JobID 3 can be performed at time t=2 giving a profit of 27.
# No more jobs can be scheduled, so total profit = 100 + 27 => 127.
# Total number of jobs completed is two (JobID 1, JobID 3). So the answer is 2 127.
#
# Constraints:
# 1 <= N <= 10^4
# 1 <= Deadline <= N
# 1 <= Profit <= 500


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
    def job_sequencing_problem_brute(self) -> None:
        pass

    def job_sequencing_problem_better(self) -> None:
        pass

    def job_sequencing_problem_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
