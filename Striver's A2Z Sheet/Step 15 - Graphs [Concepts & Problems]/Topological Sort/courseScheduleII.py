# mypy: disable-error-code="empty-body"
# QUESTION: Course Schedule II
# There are numCourses courses labelled from 0 to numCourses-1. You are given an
# array prerequisites where prerequisites[i] = [a, b] indicates that you must take
# course b before you can take course a (i.e. a directed edge b -> a).
# Return any valid ordering of courses you should take to finish all of them. If
# it is impossible to finish all courses (the prerequisite graph has a cycle),
# return an empty array.
#
# Example 1:
# Input: numCourses = 4, prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
# Output: [0, 1, 2, 3]
# Explanation: Course 0 has no prerequisites. Courses 1 and 2 require 0, and
# course 3 requires both 1 and 2. The order [0, 2, 1, 3] is also valid.
#
# Example 2:
# Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# Output: []
# Explanation: The prerequisites form a cycle, so no valid ordering exists.
#
# Constraints:
# 1 <= numCourses <= 2000
# 0 <= len(prerequisites) <= numCourses * (numCourses - 1)
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
    def course_schedule_ii_brute(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        pass

    def course_schedule_ii_better(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        pass

    def course_schedule_ii_optimal(
        self, numCourses: int, prerequisites: List[List[int]]
    ) -> List[int]:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.course_schedule_ii_optimal(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
