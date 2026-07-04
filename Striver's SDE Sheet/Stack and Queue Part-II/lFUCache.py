# mypy: disable-error-code="empty-body"
# QUESTION: LFU Cache
# Design and implement a data structure for a Least Frequently Used (LFU) cache.
# Implement the LFUCache class with the following functions:
# LFUCache(int capacity): Initializes the object with the capacity of the data structure.
# int get(int key): Returns the value of the key if it exists in the cache; otherwise returns -1.
# void put(int key, int value): Updates the value of the key if present, or inserts the key if
# not already present. When the cache reaches its capacity, it should invalidate and remove the
# least frequently used key before inserting a new item. If there is a tie (two or more keys
# with the same lowest frequency), the least recently used among them is invalidated.
# A use counter is maintained for each key: it is set to 1 when the key is inserted and
# incremented on every get or put call on that key. The functions get and put must each run in
# O(1) average time complexity.
#
# Examples:
# Example 1:
# Input: ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
#        [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output: [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# Explanation:
# LFUCache lfu = new LFUCache(2);  // initializing cache with capacity of 2
# lfu.put(1, 1);  // cache becomes [1, _], cnt(1)=1
# lfu.put(2, 2);  // cache becomes [2, 1], cnt(2)=1, cnt(1)=1
# lfu.get(1);     // returns 1; cache becomes [1, 2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);  // evicts key 2 (lowest frequency); cache becomes [3, 1], cnt(3)=1, cnt(1)=2
# lfu.get(2);     // returns -1 (not found)
# lfu.get(3);     // returns 3; cache becomes [3, 1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);  // evicts key 1 (tie on freq 2, key 1 is LRU); cache=[4, 3], cnt(4)=1, cnt(3)=2
# lfu.get(1);     // returns -1 (not found)
# lfu.get(3);     // returns 3; cache becomes [3, 4], cnt(4)=1, cnt(3)=3
# lfu.get(4);     // returns 4; cache becomes [4, 3], cnt(4)=2, cnt(3)=3
#
# Example 2:
# Input: ["LFUCache", "put", "put", "put", "put", "put", "get", "get", "get", "get", "get"]
#        [[3], [5, 7], [4, 6], [3, 5], [2, 4], [1, 3], [1], [2], [3], [4], [5]]
# Output: [null, null, null, null, null, null, 3, 4, 5, -1, -1]
# Explanation:
# LFUCache lfu = new LFUCache(3);  // initializing cache with capacity of 3
# lfu.put(5, 7);  // cache becomes [5], cnt(5)=1
# lfu.put(4, 6);  // cache becomes [4, 5], cnt(4)=1, cnt(5)=1
# lfu.put(3, 5);  // cache becomes [3, 4, 5], cnt(3)=1, cnt(4)=1, cnt(5)=1
# lfu.put(2, 4);  // evicts key 5 (lowest freq, LRU); cache=[2, 3, 4], cnt(2)=cnt(3)=cnt(4)=1
# lfu.put(1, 3);  // evicts key 4 (lowest freq, LRU); cache=[1, 2, 3], cnt(1)=cnt(2)=cnt(3)=1
# lfu.get(1);     // returns 3; cnt(1)=2
# lfu.get(2);     // returns 4; cnt(2)=2
# lfu.get(3);     // returns 5; cnt(3)=2
# lfu.get(4);     // returns -1 (not found)
# lfu.get(5);     // returns -1 (not found)
#
# Constraints:
# 1 <= capacity <= 10^3
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


class LFUCache:
    def __init__(self, capacity: int) -> None:
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass


if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))
    cache.put(3, 3)
    print(cache.get(2))
    print(cache.get(3))
