# mypy: disable-error-code="empty-body"
# QUESTION: Minimize Maximum Distance to Gas Stations
# Given a sorted array stations of existing gas-station positions and k new
# stations to add anywhere, minimize the maximum distance between two adjacent gas
# stations. Return that minimized maximum distance (real number, precision 1e-6).
# Example 1:
# Input: stations = [1,2,3,4,5,6,7,8,9,10], k = 1
# Output: 0.5
# Explanation: Placing the one new station at the midpoint of any unit gap makes
# the largest adjacent distance 0.5.
# Constraints:
# 2 <= len(stations) <= 10^4
# 1 <= k <= 10^8, stations strictly increasing.

"""
#Brute Force:
1. howMany[i] counts new stations placed in section i (between stations[i], [i+1]).
2. Repeat k times: scan all sections, compute current section length =
   (stations[i+1]-stations[i]) / (howMany[i]+1), and add the next station to the
   section with the largest current length.
3. After all k placements, the maximum section length is the answer.
TC -> O(k*N) + O(N), SC -> O(N)

#Better Approach:
1. Replace the per-step linear scan with a max-heap keyed on current section
   length. Push all sections once.
2. Repeat k times: pop the largest section, increment its count, recompute its new
   length, push it back.
3. The heap top's length after k placements is the answer.
TC -> O(N logN + k logN), SC -> O(N)

#Optimal Approach:
1. Binary search the ANSWER distance (a real number) in [0, max gap].
2. For a candidate dist, stations needed in section i is
   floor((stations[i]-stations[i-1]) / dist), minus 1 if the gap is an exact
   multiple of dist. Sum across sections.
3. If total needed > k, dist is too small -> raise low = mid; else lower high = mid.
   Use a fixed precision loop (high - low > 1e-6) instead of integer low<=high.
TC -> O(N * log(len / 1e-6)), SC -> O(1)

#KEY INSIGHT:
- Instead of deciding WHERE to place stations, binary search on the answer value:
  "can we achieve max distance <= dist with only k stations?" is monotone in dist.
"""

import heapq
from typing import List


class Solution:
    def gas_stations_brute(self, stations: List[int], k: int) -> float:
        n = len(stations)
        how_many = [0] * (n - 1)
        for _ in range(k):
            max_len, max_idx = -1.0, -1
            for i in range(n - 1):
                length = (stations[i + 1] - stations[i]) / (how_many[i] + 1)
                if length > max_len:
                    max_len = length
                    max_idx = i
            how_many[max_idx] += 1
        ans = -1.0
        for i in range(n - 1):
            ans = max(ans, (stations[i + 1] - stations[i]) / (how_many[i] + 1))
        return ans

    def gas_stations_better(self, stations: List[int], k: int) -> float:
        n = len(stations)
        how_many = [0] * (n - 1)
        pq: List[tuple[float, int]] = []
        for i in range(n - 1):
            heapq.heappush(pq, (-(stations[i + 1] - stations[i]), i))
        for _ in range(k):
            _, idx = heapq.heappop(pq)
            how_many[idx] += 1
            new_len = (stations[idx + 1] - stations[idx]) / (how_many[idx] + 1)
            heapq.heappush(pq, (-new_len, idx))
        return -pq[0][0]

    def _stations_needed(self, stations: List[int], dist: float) -> int:
        count = 0
        for i in range(1, len(stations)):
            gap = stations[i] - stations[i - 1]
            in_between = int(gap / dist)
            if gap == dist * in_between:
                in_between -= 1
            count += in_between
        return count

    def gas_stations_optimal(self, stations: List[int], k: int) -> float:
        low, high = 0.0, 0.0
        for i in range(len(stations) - 1):
            high = max(high, float(stations[i + 1] - stations[i]))
        while high - low > 1e-6:
            mid = (low + high) / 2.0
            if self._stations_needed(stations, mid) > k:
                low = mid
            else:
                high = mid
        return high


if __name__ == "__main__":
    sol = Solution()
    print(sol.gas_stations_optimal([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
