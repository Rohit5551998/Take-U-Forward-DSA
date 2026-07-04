# QUESTION: Clone Graph
# You are given a reference to a node in a connected undirected graph.
# Each node has a value `val` (unique integer from 1 to 100) and a list
# of neighbors. Return a deep copy (clone) of the graph. The cloned graph
# should have the same structure and values as the original — every node
# in the original should be replaced with a NEW node holding the same
# value, and the neighbor relationships should be preserved.
#
# Node definition:
#   class Node {
#     int val;
#     List<Node> neighbors;
#   }
#
# Examples:
# Example 1:
# Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
# Output: [[2,4],[1,3],[2,4],[1,3]]
# Explanation: The graph has 4 nodes; the deep copy preserves structure.
#
# Example 2:
# Input: adjList = [[]]
# Output: [[]]
# Explanation: A single node with no neighbors.
#
# Example 3:
# Input: adjList = []
# Output: []
# Explanation: Empty graph.
#
# Constraints:
# The number of nodes in the graph is in the range [0, 100].
# 1 <= Node.val <= 100
# Node.val is unique for each node.
# There are no self-loops or repeated edges.


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

from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List["Node"]] = None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build_graph(adj_list: List[List[int]]) -> Optional[Node]:
    # adj_list is 1-indexed (LeetCode 133): adj_list[i-1] lists neighbors of node i.
    if not adj_list:
        return None
    nodes = {i: Node(i) for i in range(1, len(adj_list) + 1)}
    for i in range(1, len(adj_list) + 1):
        nodes[i].neighbors = [nodes[j] for j in adj_list[i - 1]]
    return nodes[1]


def to_adj_list(node: Optional[Node]) -> List[List[int]]:
    # Serialize a graph (reachable from `node`) to a 1-indexed adjacency list.
    if node is None:
        return []
    visited: Dict[int, Node] = {}
    stack = [node]
    while stack:
        cur = stack.pop()
        if cur.val in visited:
            continue
        visited[cur.val] = cur
        for nb in cur.neighbors:
            if nb.val not in visited:
                stack.append(nb)
    return [sorted(nb.val for nb in visited[val].neighbors) for val in sorted(visited)]


class Solution:
    def clone_graph_brute(self, node: Optional[Node]) -> Optional[Node]:
        pass

    def clone_graph_better(self, node: Optional[Node]) -> Optional[Node]:
        pass

    def clone_graph_optimal(self, node: Optional[Node]) -> Optional[Node]:
        pass


if __name__ == "__main__":
    sol = Solution()
    node = build_graph([[2, 4], [1, 3], [2, 4], [1, 3]])
    print(to_adj_list(sol.clone_graph_optimal(node)))
