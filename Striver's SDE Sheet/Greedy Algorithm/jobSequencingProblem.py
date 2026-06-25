# QUESTION: Job sequencing Problem
# You are given a set of N jobs where each job comes with a deadline and
# a profit. The profit can only be earned upon completing the job within
# its deadline. Each job takes 1 unit of time and only one job can be
# scheduled at a time. Find:
#   1. The maximum number of jobs that can be completed.
#   2. The maximum total profit that can be earned.
# Return both values.
# Greedy approach:
#   1. Sort jobs by profit in descending order.
#   2. For each job, try to schedule it as late as possible within its
#      deadline (use a Disjoint-Set Union or a simple slot array indexed
#      by time-slot).


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
