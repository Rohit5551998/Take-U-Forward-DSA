# mypy: disable-error-code="empty-body"
# QUESTION: LRU Cache
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
# Implement the LRUCache class:
# LRUCache(int capacity): Initialize the LRU cache with positive size capacity.
# int get(int key): Returns the value of the key if the key exists, otherwise return -1.
# void put(int key, int value): Update the value of the key if the key exists. Otherwise, add
# the key-value pair to the cache. If the number of keys exceeds the capacity from this
# operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity.
# Note: Input is provided in 2D array format where the first number in each array denotes the
# operation (1 - put, 2 - get) to perform. The next integers are the values used for the
# operation.
#
# Examples:
# Example 1:
# Input: Capacity = 2,
#        nums = [[1, 1, 1], [1, 2, 2], [2, 1], [1, 3, 3], [2, 2], [1, 4, 4], [2, 1], [2, 3], [2, 4]]
# Output: [null, null, 1, null, -1, null, -1, 3, 4]
# Explanation:
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1);  // cache is {1=1}
# lRUCache.put(2, 2);  // cache is {1=1, 2=2}
# lRUCache.get(1);     // returns 1
# lRUCache.put(3, 3);  // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);     // returns -1 (not found)
# lRUCache.put(4, 4);  // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);     // returns -1 (not found)
# lRUCache.get(3);     // returns 3
# lRUCache.get(4);     // returns 4
#
# Example 2:
# Input: Capacity = 1,
#        nums = [[1, 1, 1], [1, 2, 2], [2, 1], [1, 3, 3], [2, 2], [1, 4, 4], [2, 3]]
# Output: [null, null, -1, null, -1, null, -1]
# Explanation:
# LRUCache lRUCache = new LRUCache(1);
# lRUCache.put(1, 1);  // cache is {1=1}
# lRUCache.put(2, 2);  // evicts key 1, cache is {2=2}
# lRUCache.get(1);     // returns -1 (not found)
# lRUCache.put(3, 3);  // evicts key 2, cache is {3=3}
# lRUCache.get(2);     // returns -1 (not found)
# lRUCache.put(4, 4);  // evicts key 3, cache is {4=4}
# lRUCache.get(3);     // returns -1 (not found)
#
# Constraints:
# 1 <= capacity <= 1000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 10^5 calls will be made to get and put.


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


class LRUCache:
    def __init__(self, capacity: int) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))
