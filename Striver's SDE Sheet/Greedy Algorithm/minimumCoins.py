# QUESTION: Minimum coins
# Given an integer array `coins` representing coins of different
# denominations and an integer `amount` representing a total amount of
# money, return the fewest number of coins that you need to make up that
# amount. If that amount of money cannot be made up by any combination of
# the coins, return -1.
# You have an infinite number of each kind of coin.
# Note: The Striver sheet groups this under Greedy (because the standard
# Indian/US coin systems allow a greedy solution), but for arbitrary
# denominations a DP solution is required for correctness.
#
# Examples:
# Input: coins = [1, 2, 5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1. We need 3 coins to make up the amount 11.
#
# Input : coins = [2, 5], amount = 3
# Output: -1
# Explanation: It's not possible to make amount 3 with coins 2 and 5. Since we can't
# combine coins 2 and 5 to make the amount 3, the output is -1.


"""
#Brute Force:
1. This is Coin Change (LeetCode 322), a DP problem, NOT greedy — greedy fails
   for arbitrary denominations (e.g. coins=[1,3,4], amount=6: greedy takes
   4+1+1=3, but the optimal is 3+3=2). So we explore all combinations.
2. Define find_coins(i, amount) = fewest coins to form `amount` using only
   coins[0..i]. Since supply is infinite, "taking" a coin does not consume the
   index — we can take coins[i] again.
3. Base case (i == 0, only the first coin available): if coins[0] divides
   amount exactly, we need amount // coins[0] coins; otherwise this amount is
   impossible with just coin 0, so return 10**9 (a sentinel for "infinity"). Using
   a LARGE value (not -1) is critical, because the recurrence takes a min — a
   negative sentinel would be wrongly chosen as the minimum.
4. For i > 0 there are two choices:
   - skip: don't use coins[i] at all -> find_coins(i-1, amount), add 0.
   - take: only if coins[i] <= amount, use one coins[i] and stay on index i
     (infinite supply) -> 1 + find_coins(i, amount - coins[i]).
5. Return min(take, skip). Impossible branches stay at 10**9 so min discards them.
6. The wrapper minimum_coins_brute calls find_coins(len-1, amount) and converts
   the 10**9 sentinel back to -1 (the required "cannot be made" output).
TC -> O(2^(N + amount)) — exponential branching, states recomputed repeatedly.
SC -> O(N + amount) recursion stack depth.

#Better Approach:
1. Same recurrence as the brute, but the (i, amount) state is revisited by many
   paths, causing the exponential blowup. Memoize it so each state is solved
   once.
2. Build a dp table of shape len(coins) x (amount + 1), all cells seeded to -1
   meaning "not yet computed" (safe sentinel: a real answer is >= 0, and
   impossible is stored as 10**9, so -1 never collides with a real value).
3. In find_coins_dp keep the same base case (i == 0), but for i > 0 first check
   dp[i][amount]: if it is not -1 the state is already solved, return it.
4. Otherwise compute skip and take exactly as in the brute — but recurse into
   find_coins_dp (passing dp along) so children are memoized too — then STORE
   the result in dp[i][amount] before returning.
5. The wrapper minimum_coins_better allocates dp, calls find_coins_dp, and
   converts the 10**9 sentinel to -1. Each of the N*(amount+1) states is filled
   once with O(1) work, so the exponential tree collapses to O(N*amount).
TC -> O(N * amount) — one computation per (i, amount) state.
SC -> O(N * amount) for the dp table, plus O(N + amount) recursion stack.

#Optimal Approach:
Two variants, both bottom-up tabulation (no recursion, no stack).

Variant I — 2D tabulation (minimum_coins_optimal_variant_i):
1. Same states and recurrence as the memoized "better" tier, filled iteratively
   from the base up instead of on demand. dp[i][T] = fewest coins to make T
   using coins[0..i].
2. Seed the base row (i == 0): for every T from 0..amount, dp[0][T] =
   T // coins[0] if coins[0] divides T, else 10**9.
3. Loop i from 1..len(coins)-1 (outer) and T from 0..amount (inner) — the
   opposite direction to how the recursion unwinds, so every cell a formula
   reads is already filled.
4. Copy the recurrence with table lookups: skip = dp[i-1][T]; take =
   1 + dp[i][T-coins[i]] when coins[i] <= T (stays on row i for infinite
   supply); dp[i][T] = min(skip, take).
5. Answer = dp[len-1][amount], with the 10**9 sentinel converted to -1.
TC -> O(N * amount). SC -> O(N * amount) for the full table.

Variant II — space-optimized tabulation (minimum_coins_optimal_variant_ii):
1. dp[i][...] only ever reads row i-1 (skip) and row i (take), so two 1D rows
   of length amount+1 suffice: prev (row i-1) and curr (row i).
2. Seed the base case into prev, then in the loop use prev[...] wherever the 2D
   version read dp[i-1][...] and curr[...] wherever it read dp[i][...].
3. Roll prev = curr after each coin. Read the answer from prev[amount] — when
   len(coins)==1 the loop never runs and the base row still lives in prev; when
   it runs, prev also ends on the last computed row.
TC -> O(N * amount). SC -> O(amount) — the real optimal.

#KEY INSIGHT:
- Coin Change is DP, not greedy: greedy fails for arbitrary denominations
  (coins=[1,3,4], amount=6 -> greedy 4+1+1=3, optimal 3+3=2). The recurrence
  "for each coin, min(skip it, take it and stay)" plus a +infinity sentinel for
  impossible states solves it exactly; because each dp row only depends on the
  previous row, the 2D table collapses to two 1D rows for O(amount) space.
"""

from typing import List


class Solution:
    def find_coins(self, i: int, coins: List[int], amount: int) -> int:
        mini = 10**9
        if i == 0:
            if amount % coins[i] == 0:
                mini = amount // coins[i]
            else:
                mini = 10**9
        else:
            skip = 0 + self.find_coins(i - 1, coins, amount)
            take = 10**9
            if coins[i] <= amount:
                take = 1 + self.find_coins(i, coins, amount - coins[i])
            mini = min(take, skip)
        return mini

    def minimum_coins_brute(self, coins: List[int], amount: int) -> int:
        ans = self.find_coins(len(coins) - 1, coins, amount)
        return -1 if ans == 10**9 else ans

    def find_coins_dp(self, i: int, coins: List[int], amount: int, dp: List[List[int]]) -> int:
        mini = 10**9
        if i == 0:
            if amount % coins[i] == 0:
                mini = amount // coins[i]
            else:
                mini = 10**9
        elif dp[i][amount] != -1:
            mini = dp[i][amount]
        else:
            skip = 0 + self.find_coins_dp(i - 1, coins, amount, dp)
            take = 10**9
            if coins[i] <= amount:
                take = 1 + self.find_coins_dp(i, coins, amount - coins[i], dp)
            dp[i][amount] = mini = min(take, skip)
        return mini

    def minimum_coins_better(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        ans = self.find_coins_dp(len(coins) - 1, coins, amount, dp)
        return -1 if ans == 10**9 else ans

    def minimum_coins_optimal_variant_i(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]

        for T in range(0, amount + 1):
            if T % coins[0] == 0:
                dp[0][T] = T // coins[0]
            else:
                dp[0][T] = 10**9

        for i in range(1, len(coins)):
            for T in range(0, amount + 1):
                skip = 0 + dp[i - 1][T]
                take = 10**9
                if coins[i] <= T:
                    take = 1 + dp[i][T - coins[i]]
                dp[i][T] = min(skip, take)

        ans = dp[len(coins) - 1][amount]
        return -1 if ans == 10**9 else ans

    # Space Optimized Tabulation
    """
    1. The 2D dp only ever reads row i-1 (skip) and row i (take), so replace the
       n*(amount+1) matrix with two 1D arrays of length amount+1: prev and curr.
    2. Seed the base case into prev (the i==0 row): prev[T] = T // coins[0] if
       divisible else 10**9.
    3. In the loop, wherever the 2D version read dp[i-1][...] use prev[...], and
       wherever it read dp[i][...] use curr[...].
    4. After finishing a row, roll forward: prev = curr (prev now becomes the
       "previous row" for the next coin).
    5. Return prev[amount] (NOT curr[amount]): when len(coins)==1 the loop never
       runs and the answer lives in the base row still held by prev; when it does
       run, prev ends up pointing at the last computed row too.
    NOTE: in Python `prev = curr` aliases the same list (unlike C++, which
    copies). It is harmless here because take reads already-updated cells and
    skip reads prev[T] before curr[T] is overwritten, but use curr[:] to copy if
    you want genuinely independent rows.
    """

    def minimum_coins_optimal_variant_ii(self, coins: List[int], amount: int) -> int:
        # dp = [[-1 for _ in range(amount + 1)] for _ in range(len(coins))]
        prev = [-1 for _ in range(amount + 1)]
        curr = [-1 for _ in range(amount + 1)]

        for T in range(0, amount + 1):
            if T % coins[0] == 0:
                prev[T] = T // coins[0]
            else:
                prev[T] = 10**9

        for i in range(1, len(coins)):
            for T in range(0, amount + 1):
                skip = 0 + prev[T]
                take = 10**9
                if coins[i] <= T:
                    take = 1 + curr[T - coins[i]]
                curr[T] = min(skip, take)
            prev = curr

        ans = prev[amount]
        return -1 if ans == 10**9 else ans


if __name__ == "__main__":
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    print(sol.minimum_coins_brute(coins, amount))
    coins = [1, 2, 5]
    amount = 11
    print(sol.minimum_coins_better(coins, amount))
    coins = [1, 2, 5]
    amount = 11
    print(sol.minimum_coins_optimal_variant_i(coins, amount))
    coins = [1, 2, 5]
    amount = 11
    print(sol.minimum_coins_optimal_variant_ii(coins, amount))
