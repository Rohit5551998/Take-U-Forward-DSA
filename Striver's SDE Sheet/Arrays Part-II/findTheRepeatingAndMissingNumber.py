# QUESTION: Find the repeating and missing number
# Given an integer array nums of size n containing values from [1, n] where
# each value appears exactly once in the array, except for A which appears
# twice and B which is missing. Return an array consisting of A and B in
# that order, i.e., [A, B].
#
# Examples:
# Example 1:
# Input: nums = [3, 5, 4, 1, 1]
# Output: [1, 2]
# Explanation: 1 appears twice in the array, and 2 is missing from the array. So the output is [1, 2].
#
# Example 2:
# Input: nums = [1, 2, 3, 6, 7, 5, 7]
# Output: [7, 4]
# Explanation: 7 appears twice in the array, and 4 is missing from the array. So the output is [7, 4].


"""
#Brute Force:
1. The answer is two numbers in [1, n]: one that occurs twice (A) and one that
   never occurs (B). So just interrogate every candidate value i from 1..n.
2. For each i, scan the whole array counting how many times i appears.
3. A count of 0 means i is the missing number -> ans[1] = i; a count of 2 means
   i is the repeating number -> ans[0] = i.
4. Once both slots are filled, break early. No extra structures, but the inner
   scan per candidate makes it quadratic.
TC -> O(n^2), SC -> O(1)

#Better Approach:
1. Replace the repeated inner scans with a single frequency map value -> count
   built in one pass over the array.
2. Now sweep i from 1..n and consult the map in O(1): i absent from the map is
   the missing number; i with count 2 is the repeating number.
3. Break once both are found. This swaps the brute force's O(n) inner loop for
   O(1) hashmap lookups, at the cost of O(n) space for the map.
TC -> O(n), SC -> O(n)

#Optimal Variant I — Math (sum & sum-of-squares): find_the_repeating_and_missing_number_optimal_variant_i
1. Let the array sum differ from the ideal 1..n sum by a = S - Sn. Since exactly
   A is extra and B is missing, a = A - B (every other value cancels).
2. Let the sum-of-squares differ by b = S2 - S2n = A^2 - B^2 = (A - B)(A + B).
   Dividing, c = b / a = A + B. The closed forms Sn = n(n+1)/2 and
   S2n = n(n+1)(2n+1)/6 give the ideal totals in O(1).
3. Now two linear equations: A - B = a and A + B = c. Solve them: A = (a + c)/2
   and B = c - A. Return [A, B] = [repeating, missing].
4. One pass to accumulate the two running sums, only scalars stored — no extra
   memory and no array mutation.
TC -> O(n), SC -> O(1)

#Optimal Variant II — XOR bucketing: find_the_repeating_and_missing_number_optimal_variant_ii
1. XOR all array values together with all of 1..n. Every correctly-placed value
   cancels itself, leaving xor = A ^ B (the repeating XOR the missing).
2. Isolate the lowest set bit of A ^ B: bit = xor & ~(xor - 1). A and B must
   differ in that bit, so it cleanly partitions every number into two buckets.
3. Walk array values and indices 1..n; test each with (x & bit) == 0 to route it
   into bucket xor0 (bit clear) or xor1 (bit set), XOR-ing it in. Each bucket
   cancels down to exactly one of {A, B} — one bucket holds the repeating value,
   the other the missing one.
4. Decide which bucket is the repeating one by counting occurrences of xor0 in
   the array (count 0 => xor0 is the missing one), then order [A, B] accordingly.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Two unknowns (repeating A, missing B) need two independent equations. The math
  approach gets them from sum (A-B) and sum-of-squares (A^2-B^2); the XOR approach
  gets A^B then splits the two apart on a differing bit. Both reach O(n)/O(1)
  without sorting or extra memory.
"""

from typing import List


class Solution:
    def find_the_repeating_and_missing_number_brute(self, nums: List[int]) -> List[int]:
        ans = [-1, -1]

        for i in range(1, len(nums) + 1):
            count = 0
            for j in range(0, len(nums)):
                if i == nums[j]:
                    count += 1

            if count == 0:
                ans[1] = i
            if count == 2:
                ans[0] = i
            if ans[0] != -1 and ans[1] != -1:
                break

        return ans

    def find_the_repeating_and_missing_number_better(self, nums: List[int]) -> List[int]:
        ans = [-1, -1]
        hashMap = {}

        for i in range(0, len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = 0
            hashMap[nums[i]] += 1

        for i in range(1, len(nums) + 1):
            if i not in hashMap:
                ans[1] = i
            elif hashMap[i] == 2:
                ans[0] = i
            if ans[0] != -1 and ans[1] != -1:
                break

        return ans

    def find_the_repeating_and_missing_number_optimal_variant_i(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s1 = 0
        s2 = 0
        s1n = (n * (n + 1)) // 2
        s2n = (n * (n + 1) * (2 * n + 1)) // 6
        for i in range(0, len(nums)):
            s1 += nums[i]
            s2 += nums[i] ** 2
        a = s1 - s1n
        b = s2 - s2n
        c = b // a

        x = (a + c) // 2
        y = c - x

        return [x, y]

    def find_the_repeating_and_missing_number_optimal_variant_ii(
        self, nums: List[int]
    ) -> List[int]:
        ans = [-1, -1]
        xor = 0

        for i in range(1, len(nums) + 1):
            xor ^= nums[i - 1]
            xor ^= i

        # Find the first differentiating bit from right using bit manipulation
        bit = xor & ~(xor - 1)
        # Group Numbers and Indices via bit value into one or zero club using & bit operation
        xor0, xor1 = 0, 0

        for i in range(0, len(nums)):
            if (nums[i] & bit) == 0:
                xor0 ^= nums[i]
            elif (nums[i] & bit) != 0:
                xor1 ^= nums[i]

            index = i + 1
            if (index & bit) == 0:
                xor0 ^= index
            elif (index & bit) != 0:
                xor1 ^= index

        cnt = 0
        for i in range(0, len(nums)):
            if nums[i] == xor0:
                cnt += 1

        if cnt == 0:
            ans = [xor1, xor0]
        else:
            ans = [xor0, xor1]

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3, 6, 7, 5, 7]
    print(sol.find_the_repeating_and_missing_number_brute(nums))
    nums = [1, 2, 3, 6, 7, 5, 7]
    print(sol.find_the_repeating_and_missing_number_better(nums))
    nums = [1, 2, 3, 6, 7, 5, 7]
    print(sol.find_the_repeating_and_missing_number_optimal_variant_i(nums))
    nums = [1, 2, 3, 6, 7, 5, 7]
    print(sol.find_the_repeating_and_missing_number_optimal_variant_ii(nums))
