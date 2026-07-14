# mypy: disable-error-code="empty-body"
# QUESTION: The N-th root of an integer
# Given two numbers N and M, find the Nth root of M. The N-th root of a
# number M is defined as a number X when raised to the power N equals M
# (i.e., X^N = M). If the N-th root is not an integer, return -1.
#
# Examples:
# Input: N = 3, M = 27
# Output: 3
# Explanation: The cube root of 27 is equal to 3.
#
# Input : N = 4, M = 69
# Output: -1
# Explanation : The 4th root of 69 does not exist. So, the answer is -1.


"""
#Brute Force:
1. We need the integer x such that x^n = m. Because x^n grows monotonically as
   x grows, we can simply try every candidate root starting from i = 1 upward.
2. For each i, compute i**n and compare it to m. If it equals m, i is exactly
   the n-th root, so record it in ans.
3. Key early exit: the moment i**n exceeds m, no larger i can ever satisfy
   i^n = m (the values only get bigger), so we break out immediately instead of
   scanning all the way to m. If we never hit an exact match, ans stays -1.
TC -> O(M * log N) worst case (up to M candidates when N is tiny, each power a
few ops; the early break trims this to roughly M^(1/N) iterations in practice),
SC -> O(1)

#Better Approach:
SKIPPED — there is no meaningful middle tier here. The problem goes straight
from a linear scan of the answer space (brute) to a binary search of that same
sorted answer space (optimal); no distinct intermediate algorithm exists.

#Optimal Approach:
1. The answer, if it exists, lies in the range [1, m], and x^n is monotonically
   increasing in x. A monotonic answer space is a sorted space, so we can binary
   search it instead of scanning it linearly.
2. Take mid = low + (high - low) // 2 and ask a single question: is mid^n less
   than, equal to, or greater than m? That verdict tells us which half to keep.
3. check_root(mid) computes mid^n by multiplying mid into ans n times, breaking
   early if the running product overshoots m. It returns 2 (too big), 1 (exactly
   m), or 0 (still smaller than m) — the early break also guards against building
   a needlessly huge number.
4. If the verdict is 1, mid is the exact root: store it and stop. If it is 0,
   mid^n is too small, so discard the lower half (low = mid + 1). If it is 2,
   mid^n is too big, so discard the upper half (high = mid - 1).
5. Keep halving until we either find the root or low crosses high, in which case
   no integer root exists and we return -1.
TC -> O(N * log M) (log M binary-search probes, each an O(N) power check),
SC -> O(1)

#KEY INSIGHT:
- x^n is monotonic in x, so the candidate range [1, m] is effectively a sorted
  array of "does mid^n reach m?" answers. That lets binary search replace the
  O(M) linear scan with O(log M) probes, each verified by an O(N) power check.
"""


class Solution:
    def the_n_th_root_of_an_integer_brute(self, n: int, m: int) -> int:
        ans = -1

        for i in range(1, m + 1):
            if i**n == m:
                ans = i
            elif i**n > m:
                break

        return ans

    def the_n_th_root_of_an_integer_better(self, n: int, m: int) -> int:
        # SKIP: no distinct middle tier — the problem jumps straight from a
        # linear scan of the answer space (brute) to a binary search of that
        # same sorted answer space (optimal).
        pass

    def check_root(self, mid: int, n: int, m: int) -> int:
        # Base Case ans < m
        x = 0
        ans = 1

        for _ in range(0, n):
            ans *= mid

            if ans > m:
                x = 2
                break

        if ans == m:
            x = 1

        return x

    def the_n_th_root_of_an_integer_optimal(self, n: int, m: int) -> int:
        low = 1
        high = m
        ans = -1

        while low <= high:
            mid = low + (high - low) // 2

            x = self.check_root(mid, n, m)

            if x == 1:
                ans = mid
                break

            if x == 0:
                low = mid + 1

            else:
                high = mid - 1

        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 3
    m = 27
    print(sol.the_n_th_root_of_an_integer_brute(n, m))
    n = 3
    m = 27
    print(sol.the_n_th_root_of_an_integer_optimal(n, m))
