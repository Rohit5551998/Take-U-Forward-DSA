# QUESTION: Remove duplicates from sorted array
# Given an integer array sorted in non-decreasing order, remove the
# duplicates in place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Since it
# is impossible to change the length of the array in some languages,
# you must instead have the result placed in the first part of the array
# nums. After deletion, return the number of unique elements in nums.
#
# Examples:
# Example 1:
# Input: nums = [1, 1, 2]
# Output: 2, nums = [1, 2, _]
# Explanation: Function returns 2 with the first two elements being 1 and 2.
#
# Example 2:
# Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
#
# Constraints:
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.
#
# Examples:
# Input: arr[]=[1,1,2,2,2,3,3]
# Output: [1,2,3,_,_,_,_]
# Explanation: Total number of unique elements are 3, i.e[1,2,3] and Therefore return 3 after assigning [1,2,3] in the beginning of the array.
#
# Input: arr[]=[1,1,1,2,2,3,3,3,3,4,4]
# Output: [1,2,3,4,_,_,_,_,_,_,_]
# Explanation: Total number of unique elements are 4, i.e[1,2,3,4] and Therefore return 4 after assigning [1,2,3,4] in the beginning of the array.


"""
#Brute Force:
1. We need each distinct value once, kept in order, packed at the front. The simplest way is
   to remember which values we've already emitted using a hash set.
2. Scan left to right. For each nums[i] not yet in the set, it is a first occurrence: add it
   to the set, write it at nums[index], and advance index (the write cursor for uniques).
3. Duplicates are already in the set, so they are skipped and never written. The count of
   unique elements is just the set's size.
4. Works but ignores the fact that the array is sorted, and pays O(n) extra memory for the set.
TC -> O(n), SC -> O(n)

#Better Approach:
SKIPPED — for a SORTED array there is no useful middle tier; the set-based brute drops straight
to the O(1)-space two-pointer optimal that exploits the sortedness.

#Optimal Approach:
1. Because the array is sorted, all copies of a value are adjacent, so a new unique value is
   simply one that differs from the last unique we kept — no hash set needed.
2. Keep a slow pointer i at the last written unique (starts at 0, since nums[0] is always the
   first unique) and scan a fast pointer j from 1.
3. When nums[j] != nums[i], j has reached a new distinct value: advance i and copy nums[j] into
   nums[i], growing the unique prefix by one. When they are equal, j is a duplicate and is skipped.
4. After the scan, nums[0..i] holds the uniques in order; return i + 1 as the count.
TC -> O(n), SC -> O(1)

#KEY INSIGHT:
- Sortedness makes duplicates adjacent, so "is this value new?" collapses to a single
  comparison against the previous kept element — replacing the brute's hash set with two
  pointers and O(1) space.
"""

from typing import List


class Solution:
    def remove_duplicates_from_sorted_array_brute(self, nums: List[int]) -> int:
        hashSet = set()
        index = 0
        for i in range(0, len(nums)):
            if nums[i] not in hashSet:
                hashSet.add(nums[i])

                nums[index] = nums[i]

                index += 1

        return len(hashSet)

    def remove_duplicates_from_sorted_array_better(self) -> None:
        # SKIP: for a sorted array there is no useful tier between the O(n)-space
        # hash-set brute and the O(1)-space two-pointer optimal.
        pass

    def remove_duplicates_from_sorted_array_optimal(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        return i + 1


if __name__ == "__main__":
    sol = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sol.remove_duplicates_from_sorted_array_brute(nums))
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(sol.remove_duplicates_from_sorted_array_optimal(nums))
