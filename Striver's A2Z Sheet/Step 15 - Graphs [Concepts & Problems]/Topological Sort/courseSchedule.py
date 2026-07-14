# mypy: disable-error-code="empty-body"
# QUESTION: Course Schedule I
# There are numCourses courses labelled from 0 to numCourses-1. You are given an
# array prerequisites where prerequisites[i] = [a, b] indicates that you must take
# course b before you can take course a (i.e. a directed edge b -> a).
# Return True if it is possible to finish all courses, otherwise return False.
# It is possible to finish all courses if and only if the prerequisite graph
# contains no directed cycle.
#
# Example 1:
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: True
# Explanation: To take course 1 you must first take course 0. This ordering
# (0 then 1) has no cycle, so all courses can be finished.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# Output: False
# Explanation: Course 1 requires course 0 and course 0 requires course 1, forming
# a cycle. Neither course can be started, so it is impossible to finish.
#
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= len(prerequisites) <= 5000
# prerequisites[i].length == 2
# 0 <= a, b < numCourses
# All prerequisite pairs [a, b] are distinct.

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
    def course_schedule_brute(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

    def course_schedule_better(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass

    def course_schedule_optimal(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.course_schedule_optimal(2, [[1, 0]])
