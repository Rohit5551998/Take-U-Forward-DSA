# QUESTION: Floyd Warshall Algorithm
# Given a directed, edge-weighted graph of V vertices numbered 0 to V-1,
# find the shortest distances between every pair of vertices (all-pairs
# shortest path). The graph is represented as a V x V matrix `mat`
# where mat[i][j] is the weight of the edge from i to j, or -1 if no
# direct edge exists.
# The graph may contain negative weights but no negative cycles.
# Algorithm (O(V^3)):
#   for k in 0..V-1:
#     for i in 0..V-1:
#       for j in 0..V-1:
#         dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
# Optionally detect a negative cycle by checking dist[i][i] < 0 at the end.


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


def floyd_warshall_algorithm_brute() -> None:
    pass


def floyd_warshall_algorithm_better() -> None:
    pass


def floyd_warshall_algorithm_optimal() -> None:
    pass
