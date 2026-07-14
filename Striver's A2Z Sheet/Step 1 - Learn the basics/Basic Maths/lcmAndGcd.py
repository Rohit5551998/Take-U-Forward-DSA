# mypy: disable-error-code="empty-body"
# QUESTION: LCM and GCD
# Given two positive integers a and b, compute their LCM (Least Common Multiple)
# and GCD (Greatest Common Divisor) and return them as a list [LCM, GCD].
# Uses the identity: LCM(a, b) = (a * b) / GCD(a, b).
#
# Example 1:
# Input: a = 4, b = 6
# Output: [12, 2]
# Explanation: GCD(4, 6) = 2, LCM(4, 6) = 24 / 2 = 12.
#
# Example 2:
# Input: a = 5, b = 10
# Output: [10, 5]
#
# Constraints: 1 <= a, b <= 10^4


"""
#Brute Force (lcm_and_gcd_brute):
1. The GCD is the largest number dividing both a and b, so scan candidates
   downward from min(a, b) toward 1 and take the first one dividing BOTH.
2. That first hit (the largest common divisor) is the GCD; stop immediately.
3. Derive LCM from the identity LCM = (a * b) / GCD.
TC -> O(min(a, b)), SC -> O(1)

#Better Approach:
SKIPPED — no middle tier; the downward divisor scan is replaced wholesale by the
Euclidean algorithm, with nothing sensible in between.

#Optimal Approach (lcm_and_gcd_optimal):
1. Euclid's insight: GCD(a, b) = GCD(b, a % b) — replacing the larger number by
   its remainder mod the smaller preserves the GCD while shrinking the pair fast.
2. Repeatedly reduce (subtract-via-modulo) until one value hits 0; the other is
   the GCD, since GCD(x, 0) = x.
3. Derive LCM = (a * b) / GCD from the ORIGINAL a and b (saved before reducing).
TC -> O(log(min(a, b))), SC -> O(1)

#KEY INSIGHT:
- Euclid's algorithm collapses GCD(a, b) to GCD(b, a % b): each modulo step
  shrinks the larger operand rapidly, so the GCD falls out in logarithmic time
  instead of scanning every candidate divisor.
"""

from typing import List


class Solution:
    def lcm_and_gcd_brute(self, a: int, b: int) -> List[int]:
        gcd = 1
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                gcd = i
                break
        lcm = (a * b) // gcd
        return [lcm, gcd]

    def lcm_and_gcd_better(self, a: int, b: int) -> List[int]:
        # SKIP: no middle tier — the downward divisor scan (brute) jumps straight
        # to the Euclidean algorithm (optimal).
        pass

    def lcm_and_gcd_optimal(self, a: int, b: int) -> List[int]:
        original = [a, b]
        while a > 0 and b > 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        gcd = max(a, b)
        lcm = (original[0] * original[1]) // gcd
        return [lcm, gcd]


if __name__ == "__main__":
    sol = Solution()
    print(sol.lcm_and_gcd_optimal(4, 6))
    print(sol.lcm_and_gcd_optimal(5, 10))
