# mypy: disable-error-code="empty-body"
# QUESTION: LFU Cache
# Design a Least Frequently Used (LFU) cache with a fixed capacity supporting
# get(key) and put(key, value) in O(1) average time. When capacity is exceeded,
# evict the least frequently used key; ties are broken by least recently used.
# Example 1:
# Input: LFUCache(2); put(1,1); put(2,2); get(1); put(3,3); get(2); get(3)
# Output: 1, -1, 3
# Explanation: put(3,3) evicts key 2 (freq 1, both had freq 1 but 2 was less
# recent than 1 after get(1)); get(2) is -1, get(3) is 3.
# Constraints:
# 1 <= capacity <= 10^4
# 0 <= key, value <= 10^9; up to 2*10^5 calls to get/put.

"""
#Optimal Approach:
1. Keep map[key] -> node (node stores value and its frequency cnt), and
   freqMap[freq] -> a doubly linked list (head/tail sentinels) of nodes with
   that frequency ordered by recency. Track minFreq.
2. get(key): read the value, then updateFrequency(node): unlink it from its
   current freq list, bump cnt, insert at head of the next freq list; if the old
   list becomes empty and equalled minFreq, minFreq++.
3. put(key,value): if present, update value and updateFrequency. If new and at
   capacity, evict the LRU node of the minFreq list (the tail.prev of that list),
   then insert the new node at freq 1 and reset minFreq = 1.
TC -> O(1) per op, SC -> O(capacity)

#KEY INSIGHT:
- Bucketing nodes by frequency into per-frequency LRU lists plus a minFreq
  pointer makes "least frequently, then least recently used" eviction O(1).
"""

from typing import Optional


class Node:
    def __init__(self, key: int, value: int) -> None:
        self.value = value
        self.key = key
        self.prev: Optional[Node] = None
        self.next: Optional[Node] = None
        self.cnt = 1


class DLList:
    def __init__(self) -> None:
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.freqMap: dict[int, tuple[Node, Node]] = {}
        self.map: dict[int, Node] = {}
        self.capacity = capacity
        self.minFreq = 0

    def deleteNode(self, node: Node) -> None:
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode  # type: ignore[union-attr]
        nextNode.prev = prevNode  # type: ignore[union-attr]

    def insertAtHead(self, node: Node, cnt: int) -> None:
        if cnt not in self.freqMap:
            dll = DLList()
            self.freqMap[cnt] = (dll.head, dll.tail)
        head = self.freqMap[cnt][0]
        nextNode = head.next
        head.next = node
        node.prev = head
        node.next = nextNode
        nextNode.prev = node  # type: ignore[union-attr]

    def get(self, key: int) -> int:
        ans = -1
        if key in self.map:
            node = self.map[key]
            ans = node.value
            self.updateFrequency(node)
        return ans

    def updateFrequency(self, node: Node) -> None:
        oldFreq = node.cnt
        node.cnt += 1
        self.deleteNode(node)
        if self.freqMap[oldFreq][0].next == self.freqMap[oldFreq][1]:
            del self.freqMap[oldFreq]
            if self.minFreq == oldFreq:
                self.minFreq += 1
        self.insertAtHead(node, node.cnt)

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.value = value
            self.updateFrequency(node)
        else:
            if len(self.map) == self.capacity:
                node = self.freqMap[self.minFreq][1].prev  # type: ignore[assignment]
                del self.map[node.key]
                self.deleteNode(node)
                if self.freqMap[self.minFreq][0].next == self.freqMap[self.minFreq][1]:
                    del self.freqMap[self.minFreq]
            node = Node(key, value)
            self.map[key] = node
            self.minFreq = 1
            self.insertAtHead(node, 1)


if __name__ == "__main__":
    lfu = LFUCache(2)
    lfu.put(1, 1)
    lfu.put(2, 2)
    print(lfu.get(1))
    lfu.put(3, 3)
    print(lfu.get(2))
    print(lfu.get(3))
