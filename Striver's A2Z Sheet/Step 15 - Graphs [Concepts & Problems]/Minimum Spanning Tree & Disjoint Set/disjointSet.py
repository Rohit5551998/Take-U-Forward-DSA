# mypy: disable-error-code="empty-body"
# QUESTION: Disjoint Set (Union by Rank & Path Compression)
# Implement the Disjoint Set (Union-Find) data structure supporting the
# following operations efficiently:
#   - find_parent(u): returns the ultimate parent (representative) of node u.
#   - union_by_rank(u, v): merges the sets containing u and v using union by
#     rank.
#   - union_by_size(u, v): merges the sets containing u and v using union by
#     size.
# The structure should apply path compression during find_parent so that the
# amortized time per operation approaches O(4 * alpha) ~ O(1).
#
# Example 1:
# Input:
#   Initialize a DisjointSet with 7 nodes (0..6).
#   union_by_rank(1, 2)
#   union_by_rank(2, 3)
#   union_by_rank(4, 5)
#   union_by_rank(6, 5)
#   union_by_rank(5, 3)
#   Query: are 3 and 7 in the same component?  (using nodes 0..6, ask 3 and 6)
# Output: True
# Explanation: After the unions, nodes {1,2,3,4,5,6} all belong to one
# component, so find_parent(3) == find_parent(6), meaning they are connected.
#
# Constraints:
# 1 <= number of nodes <= 10^5
# 0 <= u, v < number of nodes
# Operations may be interleaved in any order.

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


class DisjointSet:
    def __init__(self, n: int) -> None:
        self.rank: List[int] = [0] * (n + 1)
        self.size: List[int] = [1] * (n + 1)
        self.parent: List[int] = list(range(n + 1))

    def find_parent(self, node: int) -> int:
        pass

    def union_by_rank(self, u: int, v: int) -> None:
        pass

    def union_by_size(self, u: int, v: int) -> None:
        pass


if __name__ == "__main__":
    ds = DisjointSet(7)
    # ds.union_by_rank(1, 2)
    # print(ds.find_parent(3) == ds.find_parent(6))
