# QUESTION: LFU Cache
# Design and implement a data structure for a Least Frequently Used (LFU) cache. Implement the LFUCache class with the following functions: LFUCache(int capacity): Initialize the o.
#
# Examples:
# Example 1:
# Input: ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
# Output: [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# Explanation:
# LFUCache lfu = new LFUCache(2); Initializing cache with capacity of 2.
# lfu.put(1, 1); Cache becomes: [1, _], cnt(1)=1.
# lfu.put(2, 2); Cache becomes: [2, 1], cnt(2)=1, cnt(1)=1.
# lfu.get(1); Returns 1. Cache becomes: [1, 2], cnt(2)=1, cnt(1)=2.
# lfu.put(3, 3); Cache evicts 2 as it has the lowest frequency. Cache becomes: [3, 1], cnt(3)=1, cnt(1)=2.
# lfu.get(2); Returns -1 (not found).
# lfu.get(3); Returns 3. Cache becomes: [3, 1], cnt(3)=2, cnt(1)=2.
# lfu.put(4, 4); Cache evicts 1 (LRU). Cache becomes: [4, 3], cnt(4)=1, cnt(3)=2.
# lfu.get(1); Returns -1 (not found).
# lfu.get(3); Returns 3. Cache becomes: [3, 4], cnt(4)=1, cnt(3)=3.
# lfu.get(4); Returns 4. Cache becomes: [4, 3], cnt(4)=2, cnt(3)=3.
#
# Example 2:
# Input: ["LFUCache", "put", "put", "put", "put", "put", "get", "get", "get", "get", "get"]
# Output: [null, null, null, null, null, null, 3, 4, 5, -1, -1]
# Explanation:
# LFUCache lfu = new LFUCache(3); Initializing cache with capacity of 3.
# lfu.put(5, 7); Cache becomes: [5], cnt(5)=1.
# lfu.put(4, 6); Cache becomes: [4, 5], cnt(4)=1, cnt(5)=1.
# lfu.put(3, 5); Cache becomes: [3, 4, 5], cnt(3)=1, cnt(4)=1, cnt(5)=1.
# lfu.put(2, 4); Cache evicts 5 as it has the lowest frequency. Cache becomes: [2, 3, 4], cnt(2)=1, cnt(3)=1, cnt(4)=1.
# lfu.put(1, 3); Cache evicts 4 as it has the lowest frequency. Cache becomes: [1, 2, 3], cnt(1)=1, cnt(2)=1, cnt(3)=1.
# lfu.get(1); Returns 3. Cache becomes: [1, 2, 3], cnt(1)=2, cnt(2)=1, cnt(3)=1.
# lfu.get(2); Returns 4. Cache becomes: [2, 1, 3], cnt(1)=2, cnt(2)=2, cnt(3)=1.
# lfu.get(3); Returns 5. Cache becomes: [3, 2, 1], cnt(1)=2, cnt(2)=2, cnt(3)=2.
# lfu.get(4); Returns -1 (not found).
# lfu.get(5); Returns -1 (not found).


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


class Solution:
    def lfu_cache_brute(self) -> None:
        pass

    def lfu_cache_better(self) -> None:
        pass

    def lfu_cache_optimal(self) -> None:
        pass


if __name__ == "__main__":
    sol = Solution()
