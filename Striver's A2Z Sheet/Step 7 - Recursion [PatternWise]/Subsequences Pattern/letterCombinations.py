# mypy: disable-error-code="empty-body"
# QUESTION: Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter
# combinations that the number could represent (like the old telephone keypad).
# Mapping: 2->abc, 3->def, 4->ghi, 5->jkl, 6->mno, 7->pqrs, 8->tuv, 9->wxyz.
# Return the answer in any order.
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Example 2:
# Input: digits = ""
# Output: []
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].

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
    def letter_combinations_brute(self, digits: str) -> List[str]:
        pass

    def letter_combinations_better(self, digits: str) -> List[str]:
        pass

    def letter_combinations_optimal(self, digits: str) -> List[str]:
        pass


# if __name__ == "__main__":
#     sol = Solution()
#     print(sol.letter_combinations_optimal("23"))
