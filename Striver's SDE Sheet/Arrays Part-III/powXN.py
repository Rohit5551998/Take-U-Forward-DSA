# QUESTION: Pow(x, n)
# Implement the power function pow(x, n) , which calculates the x raised to n i.e. x n .
#
# Examples:
# Example 1:
# Input: x = 2.0000, n = 10
# Output: 1024.0000
# Explanation: The answer is calculated as 2^10, which equals 1024.
#
# Example 2:
# Input: x = 2.0000, n = -2
# Output: 0.2500
# Explanation: The answer is calculated as 2^(-2), which is equal to 1/4 = 0.25.


"""
#Brute Force:
1. x^n is just x multiplied by itself n times, so accumulate ans = 1 and
   multiply by x in a loop that runs n iterations.
2. A negative exponent means x^n = (1/x)^|n|. So if n < 0, replace x with its
   reciprocal 1/x and flip n positive — then the same multiply loop handles it.
3. This is the literal definition of exponentiation; correct but it does n
   multiplications, which is slow for large n.
TC -> O(n), SC -> O(1)

#Better Approach:
SKIPPED — there is no meaningful middle tier. The problem jumps straight from the
O(n) linear multiply to the O(log n) binary exponentiation; nothing sensible sits
between them.

#Optimal Approach (Binary Exponentiation):
1. Key idea: halve the exponent instead of decrementing it. Since
   x^n = (x^2)^(n/2) when n is even, every squaring of x lets us cut n in half,
   turning n multiplications into ~log2(n) of them.
2. Work with a positive copy nn = |n| (handle the sign at the very end) and a
   running result ans = 1.
3. Loop while nn > 0. When nn is even, square the base (x *= x) and halve the
   exponent (nn /= 2) — this folds the whole "x repeated nn times" into "x^2
   repeated nn/2 times" without changing the value.
4. When nn is odd, peel off one factor of the current base into the answer
   (ans *= x) and drop nn by 1, making it even so the next iteration can halve
   again. This is how the odd "leftover" gets accounted for.
5. After the loop ans holds x^|n|. If the original n was negative, take the
   reciprocal (ans = 1/ans) to get x^n.
TC -> O(log n), SC -> O(1)

#KEY INSIGHT:
- Exponentiation by squaring: because x^n = (x*x)^(n/2), squaring the base lets
  you halve the exponent each step instead of subtracting one. That collapses n
  multiplications down to O(log n), with odd exponents handled by peeling off a
  single factor before halving.
"""


class Solution:
    def pow_x_n_brute(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            x = 1 / x
            n *= -1
        for _ in range(0, n):
            ans *= x
        return ans

    def pow_x_n_better(self) -> None:
        # SKIP: no meaningful tier between O(n) linear multiply and O(log n) binary exponentiation
        pass

    def pow_x_n_optimal(self, x: float, n: int) -> float:
        ans = 1
        nn = n

        if nn < 0:
            nn *= -1

        while nn > 0:
            if nn % 2 == 0:
                nn /= 2
                x *= x
            elif nn % 2 == 1:
                nn -= 1
                ans *= x

        if n < 0:
            ans = 1 / ans
        return ans


if __name__ == "__main__":
    sol = Solution()
    x = 2.0000
    n = 10
    print(sol.pow_x_n_brute(x, n))
    x = 2.0000
    n = 10
    print(sol.pow_x_n_optimal(x, n))
