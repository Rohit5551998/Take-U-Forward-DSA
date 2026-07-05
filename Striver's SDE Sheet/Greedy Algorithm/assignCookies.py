# QUESTION: Assign Cookies
# A teacher wants to distribute cookies to students such that each
# student receives at most one cookie. Given two arrays `student` and
# `cookie`:
#   - student[i] is the greed factor of the i-th student (the minimum
#     cookie size they require to be content).
#   - cookie[j] is the size of the j-th cookie.
# A cookie j can be assigned to a student i if and only if cookie[j] >=
# student[i]. Each student gets at most one cookie; each cookie can be
# assigned to at most one student. Maximize the number of content
# students and return that count.
#
# Examples:
# Input : Student = [1, 2, 3] , Cookie = [1, 1]
# Output :1
# Explanation: Only the first cookie (1) satisfies the first student (1), therefore only
# 1 student is content.
#
# Input : Student = [1, 2] , Cookie = [1, 2, 3]
# Output : 2
# Explanation: Cookie 1 satisfies student 1 and cookie 2 satisfies student 2. Therefore,
# 2 students are content.


"""
#Brute Force:
1. Sort both `student` and `cookie` ascending first. The recursion only ever
   tries the *current* least-greedy student against the *current* smallest
   cookie, so without sorting that fixed matching order would miss valid
   pairings (e.g. student=[3,1], cookie=[1,3] would find 1 match instead of 2).
2. Define solve(i, j) = max students that can be contented using student[i:]
   and cookie[j:]. `i` is the student pointer, `j` the cookie pointer.
3. Base case: if i runs past the last student or j past the last cookie, no one
   more can be contented -> return 0.
4. If the current cookie satisfies the current student (cookie[j] >=
   student[i]), there are two real choices and we take whichever yields more:
   - assign: hand cookie j to student i -> 1 + solve(i+1, j+1). The +1 is the
     student we just contented; both pointers advance.
   - skip: hold cookie j back for a greedier student -> solve(i, j+1). Only the
     cookie pointer advances; student i keeps waiting.
5. If the current cookie is too small even for the current (least greedy
   remaining) student, it is useless to everyone left, so drop it and move to
   the next cookie -> solve(i, j+1). No max here: there is nothing to weigh.
6. Return solve(0, 0). The best count bubbles up through the max at each fork.
   Because different paths revisit the same (i, j) state, work is recomputed
   exponentially — memoizing solve(i, j) is exactly the "better" O(n*m) tier.
TC -> O(2^(N + M)) — each satisfiable state forks into assign/skip with no
reuse of subproblems (plus O(N log N + M log M) to sort).
SC -> O(N + M) recursion stack depth (ignoring the in-place sort).

#Better Approach:
1. Same recursion as the brute force, but observe that solve(i, j) is called
   with the same (i, j) many times across different paths — that repeated work
   is what makes the brute exponential. Cache each result so it is computed once.
2. Sort both arrays (same reason as brute), then build a dp table of shape
   len(student) x len(cookie), every cell seeded to -1 meaning "not computed".
   -1 is a safe sentinel because a real answer is always >= 0.
3. In solve_cookies_dp(i, j), keep the same base case (i or j past the end -> 0),
   then before doing any work check dp[i][j]: if it is not -1 the state is
   already solved, so return the cached value immediately.
4. Otherwise compute exactly as in the brute — assign (1 + solve(i+1, j+1)) vs
   skip (solve(i, j+1)) when the cookie fits, else just skip the cookie — but
   STORE the result in dp[i][j] before returning it, so any later path reuses it.
5. Return solve_cookies_dp(0, 0). Each of the N*M states is now filled once with
   O(1) work, collapsing the exponential tree to O(N*M). (This is the same set
   of states the TUF+ tabulation fills bottom-up instead of on demand.)
TC -> O(N * M) — one computation per (i, j) state (plus O(N log N + M log M) to
sort).
SC -> O(N * M) for the dp table, plus O(N + M) recursion stack depth.

#Optimal Approach:
1. Intuition: to content as many students as possible, never "waste" a large
   cookie on a low-greed student when a smaller cookie would have satisfied
   them. So we want to hand the smallest cookie that works to the least greedy
   remaining student. Sorting both arrays lets us walk them in that order.
2. Sort `student` (greed factors) and `cookie` (sizes) ascending. Now index 0
   of each is the least greedy student and the smallest cookie.
3. Keep two pointers: `left` over students (also doubles as the content count,
   since a student is only advanced once satisfied) and `right` over cookies.
4. At each step compare the current smallest unserved cookie `cookie[right]`
   with the current least greedy unserved student `student[left]`:
   - If `cookie[right] >= student[left]`, this cookie satisfies the student —
     assign it, advance `left` (one more content student) and `right`.
   - If it is too small for even the least greedy student, it is useless to
     everyone remaining (they are all greedier), so discard it by advancing
     only `right`.
5. Stop when either list is exhausted; `left` is the number of students served.
   Example: student=[1,2,3,4,5], cookie sorted=[1,3,4] → matches 1→1, 2→3,
   3→4, then cookies run out, answer 3.
TC -> O(N log N + M log M) for the two sorts; the two-pointer sweep is O(N + M).
SC -> O(1) auxiliary (ignoring the in-place sort's stack).

#KEY INSIGHT:
- Sort both, then greedily give the smallest cookie that works to the least
  greedy remaining student. A cookie too small for the least greedy student is
  too small for everyone left, so it can be dropped with no regret — this lets
  a single forward sweep of both sorted arrays find the maximum matching.
"""

from typing import List


class Solution:
    def solve_cookies(self, i: int, j: int, student: List[int], cookie: List[int]) -> int:
        if i >= len(student) or j >= len(cookie):
            return 0
        if cookie[j] >= student[i]:
            assign = self.solve_cookies(i + 1, j + 1, student, cookie) + 1
            skip = self.solve_cookies(i, j + 1, student, cookie)
            return max(assign, skip)
        return self.solve_cookies(i, j + 1, student, cookie)

    def assign_cookies_brute(self, student: List[int], cookie: List[int]) -> int:
        student.sort()
        cookie.sort()

        return self.solve_cookies(0, 0, student, cookie)

    def solve_cookies_dp(
        self, i: int, j: int, student: List[int], cookie: List[int], dp: List[List[int]]
    ) -> int:
        if i >= len(student) or j >= len(cookie):
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        if cookie[j] >= student[i]:
            assign = self.solve_cookies_dp(i + 1, j + 1, student, cookie, dp) + 1
            skip = self.solve_cookies_dp(i, j + 1, student, cookie, dp)
            dp[i][j] = max(assign, skip)
        else:
            dp[i][j] = self.solve_cookies_dp(i, j + 1, student, cookie, dp)
        return dp[i][j]

    def assign_cookies_better(self, student: List[int], cookie: List[int]) -> int:
        student.sort()
        cookie.sort()

        dp = [[-1 for _ in range(len(cookie))] for _ in range(len(student))]
        return self.solve_cookies_dp(0, 0, student, cookie, dp)

    def assign_cookies_optimal(self, student: List[int], cookie: List[int]) -> int:
        student.sort()
        cookie.sort()
        left = right = 0
        while left < len(student) and right < len(cookie):
            if cookie[right] >= student[left]:
                left += 1
            right += 1

        return left


if __name__ == "__main__":
    sol = Solution()
    student = [1, 2, 3, 4, 5]
    cookie = [1, 4, 3]
    # student = [10, 9, 8, 7]
    # cookie = [5, 6, 7, 8]
    print(sol.assign_cookies_brute(student, cookie))
    student = [1, 2, 3, 4, 5]
    cookie = [1, 4, 3]
    # student = [10, 9, 8, 7]
    # cookie = [5, 6, 7, 8]
    print(sol.assign_cookies_better(student, cookie))
    student = [1, 2, 3, 4, 5]
    cookie = [1, 4, 3]
    # student = [10, 9, 8, 7]
    # cookie = [5, 6, 7, 8]
    print(sol.assign_cookies_optimal(student, cookie))
