# mypy: disable-error-code="empty-body"
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
SKIPPED — the only brute is generating all 2^N subsets of jobs and keeping the
best feasible one, an exponential O(2^N) approach, not a normal-complexity tier
worth implementing.

#Better Approach:
SKIPPED — no distinct tier exists between the exponential brute and the greedy
optimal; the sort-by-profit + slot-array greedy is the single polynomial approach.

#Optimal Approach:
1. Greedy: a job only earns if done by its deadline, and each slot holds one
   job — so to maximise profit, consider jobs in DESCENDING profit order and
   give each the LATEST free slot on or before its deadline.
2. Sort jobs by profit descending, so the most valuable jobs claim slots first.
3. Find maxDeadline and make a slot array hashArray[1..maxDeadline], all -1
   (free); index t represents the time unit t.
4. For each job (richest first), scan slots from its deadline down to 1 and take
   the first free one: mark it with the job id, add the profit, bump the count,
   and stop.
5. Choosing the LATEST free slot (not the earliest) is the crux — it leaves the
   lower-numbered slots open for later jobs that have tighter deadlines and so
   can only sit early.
TC -> O(n log n + n*maxDeadline) (sort + per-job slot scan),
SC -> O(maxDeadline) for the slot array

#KEY INSIGHT:
- Process jobs by decreasing profit and place each in the latest still-free slot
  before its deadline. "Latest slot" is what makes it optimal: it greedily
  protects earlier time units for the tighter-deadline jobs still to be placed,
  so no high-profit job is ever needlessly displaced.
"""

from typing import List


class Solution:
    def job_sequencing_problem_brute(self, jobs: List[List[int]]) -> List[int]:
        # SKIP: only brute is exponential O(2^N) subset enumeration, not a normal-complexity tier
        pass

    def job_sequencing_problem_better(self, jobs: List[List[int]]) -> List[int]:
        # SKIP: no distinct tier between the exponential brute and the greedy optimal
        pass

    def job_sequencing_problem_optimal(self, jobs: List[List[int]]) -> List[int]:
        jobs.sort(key=lambda item: item[2], reverse=True)

        maxDeadline = max(jobs, key=lambda item: item[1])[1]
        hashArray = [-1 for _ in range(0, maxDeadline + 1)]
        jobsCount = 0
        totalProfit = 0

        for i in range(0, len(jobs)):
            for j in range(jobs[i][1], 0, -1):
                if hashArray[j] == -1:
                    hashArray[j] = jobs[i][0]
                    jobsCount += 1
                    totalProfit += jobs[i][2]
                    break

        return [jobsCount, totalProfit]


if __name__ == "__main__":
    sol = Solution()
    jobs = [[1, 4, 20], [2, 1, 10], [3, 1, 40], [4, 1, 30]]
    print(sol.job_sequencing_problem_optimal(jobs))
