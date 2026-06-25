# QUESTION: Next Permutation
# Given an array Arr[] of integers, rearrange the numbers of the given array
# into the lexicographically next greater permutation of numbers. If such an
# arrangement is not possible, it must rearrange it as the lowest possible
# order (i.e., sorted in ascending order). The replacement must be in place
# and use only constant extra memory.
#
# Examples:
# Example 1:
# Input: Arr[] = {1,3,2}
# Output: {2,1,3}
# Explanation: All permutations of {1,2,3} are {{1,2,3}, {1,3,2}, {2,1,3},
# {2,3,1}, {3,1,2}, {3,2,1}}. The next permutation just after {1,3,2} is {2,1,3}.
#
# Example 2:
# Input: Arr[] = {3,2,1}
# Output: {1,2,3}
# Explanation: {3,2,1} is the last permutation, so we wrap around and return
# the lowest permutation {1,2,3}.
#
# Example 3:
# Input: Arr[] = {1,1,5}
# Output: {1,5,1}
#
# Constraints:
# 1 <= Arr.length <= 100
# 0 <= Arr[i] <= 100

"""
#Brute Force:
SKIPPED - Generate all permutations recursively, sort them lexicographically,
then find the current one and return the next (wrap to first if it's the last).
TC -> O(N! * N), SC -> O(N! * N)

#Better Approach:
SKIPPED - Use the built-in next_permutation from the C++ STL (<algorithm>).
TC -> O(N), SC -> O(1)

#Optimal Approach:
1. The next permutation must be the *smallest* arrangement that is still strictly
   larger than the current one. A trailing suffix that is already in descending
   order (e.g. 5,4,3,0,0) is the largest that suffix can ever be, so nothing inside
   it can grow — the change has to happen at the element just before that suffix.
2. Scan from the right and find the first "pivot" index where arr[i-1] < arr[i].
   That breakpoint marks where the descending tail begins; arr[index] (=arr[i-1])
   is the digit we must increase. If no such pivot exists, the whole array is
   descending (the last permutation) → reverse it to wrap back to the smallest one.
3. To increase arr[index] as little as possible, scan the descending tail from the
   right and swap arr[index] with the first element greater than it. Since the tail
   is descending, the rightmost element greater than the pivot is the smallest valid
   candidate, giving the minimal bump.
4. After the swap the tail is still descending. To make the whole number as small as
   possible we reverse that tail (everything after index) into ascending order.
   Reversing a descending run = sorting it ascending in O(len) without a sort call.
TC -> O(N), SC -> O(1)

#KEY INSIGHT:
- The next permutation changes exactly one "pivot" digit — the first drop from the
  right (arr[i-1] < arr[i]). Swap it with the smallest tail element still larger than
  it, then reverse the (already descending) tail to ascending. No pivot ⇒ reverse all.
"""

from typing import List


class Solution:
    def next_permutation_brute(self) -> None:
        # SKIP: brute force is generating all permutations recursively then picking
        # the next one lexicographically (O(N! * N)) — too slow to bother coding.
        pass

    def next_permutation_better(self) -> None:
        # SKIP: better approach is C++ STL's std::next_permutation, not applicable in Python.
        pass

    def reverse(self, start: int, end: int, arr: List[int]) -> None:
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    def next_permutation_optimal(self, arr: List[int]) -> List[int]:
        index = -1

        for i in range(len(arr) - 1, 0, -1):
            if arr[i] > arr[i - 1]:
                index = i - 1
                break

        if index == -1:
            self.reverse(0, len(arr) - 1, arr)
        else:
            for i in range(len(arr) - 1, index, -1):
                if arr[i] > arr[index]:
                    arr[i], arr[index] = arr[index], arr[i]
                    break

            self.reverse(index + 1, len(arr) - 1, arr)

        return arr


if __name__ == "__main__":
    sol = Solution()
    arr = [2, 1, 5, 4, 3, 0, 0]
    print(sol.next_permutation_optimal(arr))
