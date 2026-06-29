# QUESTION: Count subarrays with given xor K
# Given an array of integers A and an integer B. Find the total number of subarrays having bitwise XOR of all elements equal to k.
#
# Examples:
# Input: A = [4, 2, 2, 6, 4] , k = 6
# Output: 4
# Explanation: The subarrays having XOR of their elements as 6 are [4, 2], [4, 2, 2, 6, 4], [2, 2, 6], [6]
#
# Input: A = [5, 6, 7, 8, 9], k = 5
# Output: 2
# Explanation: The subarrays having XOR of their elements as 5 are [5] and [5, 6, 7, 8, 9]


"""
#Brute Force:
1. The count of subarrays with XOR == k is unknown, so enumerate EVERY subarray.
   Fix a start i and an end j, giving the subarray nums[i..j].
2. For each (i, j) compute its XOR from scratch with an innermost loop over
   k in [i..j], accumulating xor ^= nums[k].
3. If that xor equals target, this subarray qualifies, so count += 1.
4. Three nested loops (start, end, recompute) make this the costliest version.
TC -> O(n^3), SC -> O(1)

#Better Approach:
1. The wasteful part above is recomputing the XOR for every (i, j) from scratch.
   Fix the start i, then sweep the end j rightward keeping a running xor.
2. xor ^= nums[j] extends the previous subarray's XOR by one element in O(1),
   so we never recompute — the inner k-loop is gone.
3. Whenever xor == target, count += 1. Repeat for every start i.
TC -> O(n^2), SC -> O(1)

#Optimal Approach:
1. Use prefix XOR: prefixXor after index i is the XOR of nums[0..i]. The XOR of
   a subarray (j+1..i) equals prefixXor[i] ^ prefixXor[j] (shared prefix cancels).
2. We want that subarray XOR to be target, i.e. prefixXor[i] ^ prefixXor[j] == target.
   XOR-rearranging (XOR is its own inverse) gives prefixXor[j] == prefixXor[i] ^ target.
3. So at index i, the number of valid subarrays ending here = how many earlier
   prefixes equalled rem = prefixXor ^ target. A hashMap of prefix-XOR -> frequency
   gives that count in O(1).
4. Seed hashMap[0] = 1 BEFORE the loop: an empty prefix has XOR 0, which lets a
   subarray starting at index 0 (whose whole prefixXor itself == target) be counted.
5. For each element: update prefixXor, add hashMap[rem] to count (if present), then
   record the current prefixXor by incrementing its frequency for future indices.
6. Note we store FREQUENCIES, not earliest index — this is a COUNT problem (every
   matching prefix contributes a subarray), unlike longest-length problems.
TC -> O(n), SC -> O(n)

#KEY INSIGHT:
- prefixXor[i] ^ prefixXor[j] == target  <=>  prefixXor[j] == prefixXor[i] ^ target.
  Because XOR is its own inverse, "find subarrays with XOR k" becomes "count earlier
  prefixes equal to prefixXor ^ k" — an O(1) hashMap lookup per element. Seeding {0:1}
  handles subarrays that start at index 0.
"""

from typing import List


class Solution:
    def count_subarrays_with_given_xor_k_brute(self, nums: List[int], target: int) -> int:
        count = 0

        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                xor = 0
                for k in range(i, j + 1):
                    xor ^= nums[k]
                if xor == target:
                    count += 1

        return count

    def count_subarrays_with_given_xor_k_better(self, nums: List[int], target: int) -> int:
        count = 0

        for i in range(0, len(nums)):
            xor = 0
            for j in range(i, len(nums)):
                xor ^= nums[j]
                if xor == target:
                    count += 1
        return count

    def count_subarrays_with_given_xor_k_optimal(self, nums: List[int], target: int) -> int:
        hashMap = {}
        count = 0
        prefixXor = 0

        # Seed with prefixXor 0 seen once: the empty prefix has XOR 0, so a subarray
        # starting at index 0 (whose own prefixXor == target) gets counted.
        hashMap[0] = 1

        for i in range(0, len(nums)):
            prefixXor ^= nums[i]

            # We need an earlier prefix j with prefixXor[j] == prefixXor[i] ^ target,
            # because then subarray (j+1..i) has XOR == target. rem is that wanted prefix.
            rem = prefixXor ^ target

            # Every earlier index with that prefix gives one valid subarray ending here,
            # so add its frequency (not just 1) to the count.
            if rem in hashMap:
                count += hashMap[rem]

            # Record the current prefixXor's frequency for future indices to match against.
            if prefixXor not in hashMap:
                hashMap[prefixXor] = 0
            hashMap[prefixXor] += 1

        return count


if __name__ == "__main__":
    sol = Solution()
    nums = [4, 2, 2, 6, 4]
    k = 6
    print(sol.count_subarrays_with_given_xor_k_brute(nums, k))
    nums = [4, 2, 2, 6, 4]
    k = 6
    print(sol.count_subarrays_with_given_xor_k_better(nums, k))
    nums = [4, 2, 2, 6, 4]
    k = 6
    print(sol.count_subarrays_with_given_xor_k_optimal(nums, k))
