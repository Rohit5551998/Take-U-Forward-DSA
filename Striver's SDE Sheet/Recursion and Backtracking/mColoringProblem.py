# mypy: disable-error-code="empty-body"
# QUESTION: M Coloring Problem
# Given an integer M and an undirected graph with N vertices (zero indexed) and E edges. The goal
# is to determine whether the graph can be coloured with a maximum of M colors so that no two of
# its adjacent vertices have the same colour applied to them. In this context, colouring a graph
# refers to giving each vertex a colour. If the colouring of vertices is possible then return
# true, otherwise return false.
#
# Examples:
# Example 1:
# Input: N = 4, M = 3, E = 5, Edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]
# Output: true
# Explanation: Consider the three colors to be red, green, blue.
# We can color vertex 0 with red, vertex 1 with blue, vertex 2 with green, vertex 3 with blue.
# In this way we can color the graph using 3 colors at most.
#
# Example 2:
# Input: N = 3, M = 2, E = 3, Edges = [(0, 1), (1, 2), (0, 2)]
# Output: false
# Explanation: Consider the two colors to be red, green.
# We can color vertex 0 with red and vertex 1 with green.
# As vertex 2 is adjacent to both vertex 1 and vertex 0, it can be colored with neither red nor
# green. Hence, as we could not color all vertices of the graph, we return false.
#
# Constraints:
# - 1 <= N <= 20
# - 1 <= E <= (N*(N-1)/2)
# - 1 <= M <= N


"""
#Brute Force:
SKIPPED — no distinct cruder tier. The only naive alternative (generate all m^n
color assignments and test each against every edge) is just this backtracking
WITHOUT the is_safe pruning — same exponential class, not a separate approach.

#Better Approach:
SKIPPED — no middle tier. M-Coloring is a single constraint-satisfaction
backtracking; nothing sensible sits between "brute enumerate" and the pruned
backtracking below.

#Optimal Approach (is_safe + color_nodes + m_coloring_problem_optimal):
1. Represent the graph for fast adjacency tests: dump the edge list into a set of
   tuples (one direction each). Then "is u adjacent to v?" is an O(1) lookup of
   (u,v)/(v,u) in the set instead of scanning the whole edge list every time.
2. colors[] starts all -1 meaning "uncolored". Using -1 (NOT 0) as the sentinel
   is deliberate: real colors are 0..m-1, so an unpainted node can never be
   mistaken for a node genuinely painted color 0.
3. Color one node at a time in index order (node = 0..n-1). At each node try every
   color i in 0..m-1 as a candidate.
4. is_safe(node, i): loop over all other nodes k; the color is unsafe iff some k
   is adjacent to node ((k,node) or (node,k) in the set) AND already holds color i
   (colors[k] == i). Uncolored neighbors are -1 so they never trigger a conflict.
5. If i is safe, paint colors[node] = i and RECURSE to node+1. If that returns
   True, a full valid coloring exists — set ans True and stop.
6. Backtrack: if the recursion fails, reset colors[node] = -1 (the sentinel) so a
   discarded node leaves no phantom color behind for later is_safe checks.
7. Base case: node == n means every vertex is painted without conflict — return
   True. If the loop exhausts all m colors with no success, return False so the
   caller backtracks (ans defaults to False to make this path explicit).
TC -> O(m^n * n), SC -> O(n) colors + O(e) edge set + O(n) recursion depth
   (up to m^n color combinations across n vertices; each is_safe scans O(n) nodes)

#KEY INSIGHT:
- Backtracking with a per-vertex safety check: paint a vertex only with a color no
  adjacent vertex already uses, recurse, and retract on failure. Two details make
  it clean — an edge SET for O(1) adjacency tests, and a -1 sentinel distinct from
  the real colors so partially/backtracked state never fabricates a false clash.
"""

from typing import List


class Solution:
    def m_coloring_problem_brute(self, n: int, m: int, edges: List[List[int]]) -> bool:
        # SKIP: no distinct cruder tier — "test all m^n assignments" is just the
        # backtracking below minus the is_safe pruning, same exponential class.
        pass

    def m_coloring_problem_better(self, n: int, m: int, edges: List[List[int]]) -> bool:
        # SKIP: no middle tier — single constraint-satisfaction backtracking;
        # nothing sensible sits between brute enumeration and the pruned version.
        pass

    def is_safe(self, n: int, edges: set, colors: List[int], node: int, color: int) -> bool:
        ans = True
        for k in range(0, len(colors)):
            if k != node and ((k, node) in edges or (node, k) in edges) and colors[k] == color:
                ans = False
                break
        return ans

    def color_nodes(self, n: int, m: int, edges: set, colors: List[int], node: int) -> bool:
        ans = False
        if node == n:
            ans = True

        else:
            for i in range(0, m):
                if self.is_safe(n, edges, colors, node, i):
                    colors[node] = i
                    if self.color_nodes(n, m, edges, colors, node + 1) == True:
                        ans = True
                        break
                    colors[node] = -1

        return ans

    def m_coloring_problem_optimal(self, n: int, m: int, edges: List[List[int]]) -> bool:
        colors = [-1 for _ in range(n)]
        hashSet = set()
        for u, v in edges:
            hashSet.add((u, v))
        ans = self.color_nodes(n, m, hashSet, colors, 0)
        return ans


if __name__ == "__main__":
    sol = Solution()
    n = 4
    m = 3
    edges = [[0, 1], [1, 2], [2, 3], [3, 0], [0, 2]]
    print(sol.m_coloring_problem_optimal(n, m, edges))
