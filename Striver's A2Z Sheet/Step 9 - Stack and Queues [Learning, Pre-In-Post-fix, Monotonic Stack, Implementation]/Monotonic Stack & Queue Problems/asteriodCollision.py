# mypy: disable-error-code="empty-body"
# QUESTION: Asteroid Collision
# Given an array of asteroids, each value's sign is its direction (+ right, -
# left) and its magnitude is its size. Asteroids moving toward each other
# collide: the smaller explodes; equal sizes both explode. Same-direction
# asteroids never collide. Return the state after all collisions.
# Example 1:
# Input: arr = [-3, 4, 7, 1, 1, 2, -3, -7, 17, 15, -18, -19]
# Output: [-3, -18, -19]
# Explanation: The initial -3 survives (nothing to its left). The block
# 4,7,1,1,2 is a rightward group; the later -3 is destroyed by 7, and -7 cancels
# equal-sized 7; 17,15 are destroyed by -18, and -18,-19 survive.
# Constraints:
# 2 <= n <= 10^4
# -1000 <= arr[i] <= 1000, arr[i] != 0

"""
#Optimal Approach:
1. Iterate left to right using a stack of surviving asteroids.
2. A positive (right-moving) asteroid can never collide with what's already on
   the stack in the future, so push it.
3. A negative (left-moving) asteroid collides with positive tops smaller than
   its magnitude — pop them. If the top equals its magnitude, both explode (pop,
   don't push). If the stack is empty or the top is also negative, it survives —
   push it.
TC -> O(N), SC -> O(N)

#KEY INSIGHT:
- Only a right-moving asteroid followed by a left-moving one can collide, so a
  stack of "so far surviving" asteroids resolves every collision in one pass.
"""


class Solution:
    def findSolution(self, arr: list[int]) -> list[int]:
        st: list[int] = []
        for i in range(len(arr)):
            if arr[i] > 0:
                st.append(arr[i])
            else:
                while st and st[-1] > 0 and st[-1] < abs(arr[i]):
                    st.pop()
                if st and st[-1] == abs(arr[i]):
                    st.pop()
                elif not st or st[-1] < 0:
                    st.append(arr[i])
        return st


if __name__ == "__main__":
    print(Solution().findSolution([-3, 4, 7, 1, 1, 2, -3, -7, 17, 15, -18, -19]))
