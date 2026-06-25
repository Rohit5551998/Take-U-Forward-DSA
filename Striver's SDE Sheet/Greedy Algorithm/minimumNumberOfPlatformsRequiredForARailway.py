# QUESTION: Minimum number of platforms required for a railway
# We are given two arrays `arr` and `dep` of size N, representing the
# arrival and departure times of N trains that stop at a railway
# station. Find the minimum number of platforms needed so that no train
# has to wait.
# Note: If a train arrives at exactly the same time another train
# departs, they cannot share a platform (they need separate platforms).
# Greedy approach:
#   1. Sort both arrival and departure arrays independently.
#   2. Use two pointers; iterate through merged events. When you see an
#      arrival before the next departure, you need an extra platform; on
#      a departure before the next arrival, you free one.
#   3. Track the running max of simultaneous trains — that's the answer.
#
# Examples:
# Input: N=6,
# arr[] = {9:00, 9:45, 9:55, 11:00, 15:00, 18:00}
# dep[] = {9:20, 12:00, 11:30, 11:50, 19:00, 20:00}
# Output: 3
# Explanation: There are at-most three trains at a time. The train at 11:00 arrived but the trains which had arrived at 9:45 and 9:55 have still not departed. So, we need at least three platforms here.
#
# Input : N=2,
# arr[]={10:20,12:00}
# dep[]={10:50,12:30}
# Output: 1
# Explanation : Before the arrival of the new train, the earlier train already departed. So, we don't require multiple platforms.


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
    def minimum_number_of_platforms_required_for_a_railway_brute(self) -> None:
        pass

    def minimum_number_of_platforms_required_for_a_railway_better(self) -> None:
        pass

    def minimum_number_of_platforms_required_for_a_railway_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
