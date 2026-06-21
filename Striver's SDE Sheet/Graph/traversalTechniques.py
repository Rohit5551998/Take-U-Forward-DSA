# QUESTION: Traversal Techniques
# Given an undirected graph (represented as an adjacency list), return
# the BFS and DFS traversals starting from vertex 0 (or 1, depending on
# the convention).
# (Striver's sheet groups BFS + DFS basics under this entry. This is a
# meta-problem — implementing both to ensure you have the patterns down.)
#
# BFS Traversal:
#   1. Start at the source, mark it visited, enqueue.
#   2. Pop the front, append to result, then enqueue all unvisited
#      neighbors (mark them visited as they're enqueued).
#   3. Repeat until queue is empty.
#
# DFS Traversal:
#   1. Start at the source, mark it visited, append to result.
#   2. Recursively DFS into each unvisited neighbor.
#
# Both produce a list of all reachable nodes from the source in their
# respective traversal orders.


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


def traversal_techniques_brute() -> None:
    pass


def traversal_techniques_better() -> None:
    pass


def traversal_techniques_optimal() -> None:
    pass
