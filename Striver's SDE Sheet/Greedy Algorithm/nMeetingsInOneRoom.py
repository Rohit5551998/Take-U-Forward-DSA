# QUESTION: N meetings in one room
# There is one meeting room in a firm. You are given two arrays `start`
# and `end`, each of size N. For index i, start[i] denotes the starting
# time of the i-th meeting while end[i] denotes its ending time.
# A meeting can be scheduled if the room is free at its starting time
# (i.e., no other meeting is currently being held). Two meetings cannot
# overlap — but a meeting starting at the exact end time of another is
# allowed.
# Find the maximum number of meetings that can be held in the room (and
# optionally, the indices of those meetings).
# Greedy approach: sort meetings by END time ascending; pick a meeting
# whenever its start time >= the last selected meeting's end time.
#
# Examples:
# Input: N = 6, start[] = {1,3,0,5,8,5}, end[] = {2,4,5,7,9,9}
# Output: [1, 2, 4, 5]
# Explanation: These meeting can be conducted in the room.
#
# Input: N = 2, start[] = {1,5}, end[] = {7,8}
# Output: [1]
# Explanation: Any one out of the two meeting can take place.


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


def n_meetings_in_one_room_brute() -> None:
    pass


def n_meetings_in_one_room_better() -> None:
    pass


def n_meetings_in_one_room_optimal() -> None:
    pass
