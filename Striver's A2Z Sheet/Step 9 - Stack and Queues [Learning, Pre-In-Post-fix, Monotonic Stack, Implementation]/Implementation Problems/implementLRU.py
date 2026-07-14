# mypy: disable-error-code="empty-body"
# QUESTION: LRU Cache
# Design a Least Recently Used (LRU) cache with a fixed capacity supporting
# get(key) and put(key, value) in O(1) average time. When capacity is exceeded,
# evict the least recently used entry.
# Example 1:
# Input: LRUCache(2); put(1,1); put(2,2); get(1); put(3,3); get(2)
# Output: 1, -1
# Explanation: get(1) returns 1 and marks 1 as recent; put(3,3) evicts key 2
# (least recently used), so get(2) returns -1.
# Constraints:
# 1 <= capacity <= 3000
# 0 <= key, value <= 10^4; up to 2*10^5 calls to get/put.

"""
#Optimal Approach:
1. Combine a hashmap (key -> node) with a doubly linked list ordered by recency;
   dummy head/tail sentinels simplify edge cases. Head side = most recent.
2. get(key): if present, unlink the node and re-insert it right after head
   (mark as most recently used), return its value; else -1.
3. put(key,value): if present, update value and move to head. If new and at
   capacity, evict the node before tail (least recently used) and drop it from
   the map; then insert the new node at head.
TC -> O(1) per op, SC -> O(capacity)

#KEY INSIGHT:
- The hashmap gives O(1) lookup while the doubly linked list gives O(1)
  reordering/eviction; together they make both operations O(1).
"""

from typing import Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.value = value
        self.key = key
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map: dict[int, Node] = {}
        self.capacity = capacity

    def deleteNode(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode  # type: ignore[union-attr]
        nextNode.prev = prevNode  # type: ignore[union-attr]

    def insertAtHead(self, node: Node) -> None:
        nextNode = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = nextNode
        nextNode.prev = node  # type: ignore[union-attr]

    def get(self, key: int) -> int:
        ans = -1
        if key in self.map:
            node = self.map[key]
            ans = node.value
            self.deleteNode(node)
            self.insertAtHead(node)
        return ans

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self.deleteNode(node)
            self.insertAtHead(node)
            node.value = value
        else:
            if len(self.map) == self.capacity:
                lruNode = self.tail.prev
                del self.map[lruNode.key]  # type: ignore[union-attr]
                self.deleteNode(lruNode)  # type: ignore[arg-type]
            node = Node(key, value)
            self.map[key] = node
            self.insertAtHead(node)


if __name__ == "__main__":
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    print(lru.get(1))
    lru.put(3, 3)
    print(lru.get(2))
