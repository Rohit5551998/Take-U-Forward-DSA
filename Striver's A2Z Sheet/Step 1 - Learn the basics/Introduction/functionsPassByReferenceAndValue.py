# mypy: disable-error-code="empty-body"
# QUESTION: Functions (Pass by Reference and Value)
# Foundational/theory topic: functions package reusable logic. Arguments may be
# passed by value (a copy is made, caller unaffected) or by reference (the callee
# can mutate the caller's object). Python passes object references; immutable
# objects behave like pass-by-value, mutable ones like pass-by-reference.
# Example 1:
# Input: lst = [1, 2, 3]; function appends 4 in place
# Output: [1, 2, 3, 4]
# Explanation: A list is mutable, so the change is visible to the caller.
# Constraints:
# - Rebinding a parameter inside a function does not affect the caller.
# - Mutating a shared mutable object does affect the caller.

"""
#Brute Force:
1.
TC -> O(), SC -> O()

#Better Approach:
1.
TC -> O(), SC -> O()

#Optimal Approach:
1.
TC -> O(), SC -> O()

#KEY INSIGHT:
-
"""

from typing import List


class Solution:
    def functions_pass_by_reference_and_value_brute(self, lst: List[int]) -> None:
        pass

    def functions_pass_by_reference_and_value_better(self, lst: List[int]) -> None:
        pass

    def functions_pass_by_reference_and_value_optimal(self, lst: List[int]) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
    # sol.functions_pass_by_reference_and_value_optimal(...)
