class Node: 
  def __init__(self, key: int, value: int):
    self.value = value
    self.key = key
    self.prev = None
    self.next = None
    self.cnt = 1

class LRUCache:
  def __init__(self):
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    self.head.next = self.tail
    self.tail.prev = self.head

class LFUCache:
  def __init__(self, capacity: int):
    self.freqMap = {}
    self.map = {}
    self.capacity = capacity
    self.minFreq = 0

  def deleteNode(self, node: Node):
    prevNode = node.prev
    nextNode = node.next
    prevNode.next = nextNode
    nextNode.prev = prevNode

  def insertAtHead(self, node: Node, cnt: int):
    if (cnt not in self.freqMap):
      lru = LRUCache()
      self.freqMap[cnt] = (lru.head, lru.tail)

    head = self.freqMap[cnt][0]
    nextNode = head.next
    head.next = node
    node.prev = head
    node.next = nextNode
    nextNode.prev = node

  def get(self, key: int) -> int:
    ans = -1
    if (key in self.map):
      node = self.map[key]
      ans = node.value
      self.updateFrequency(node)
    return ans

  def updateFrequency(self, node):
    oldFreq = node.cnt
    node.cnt += 1
    self.deleteNode(node)

    #Check if head of current node's linked list is equal to it's tail
    if (self.freqMap[oldFreq][0].next == self.freqMap[oldFreq][1]):
      del self.freqMap[oldFreq]

      #Check if minimum frequency need to be updated or not
      if (self.minFreq == oldFreq):
        self.minFreq += 1
    
    self.insertAtHead(node, node.cnt)

  def put(self, key: int, value: int) -> None:
    if (key in self.map):
      node = self.map[key]
      node.value = value
      self.updateFrequency(node)

    else:
      if (len(self.map.values()) == self.capacity):
        node = self.freqMap[self.minFreq][1].prev
        del self.map[node.key]
        self.deleteNode(node)

        #Check whether minimum frequency list is empty or not
        if (self.freqMap[self.minFreq][0].next == self.freqMap[self.minFreq][1]):
          del self.freqMap[self.minFreq]

      node = Node(key, value)
      self.map[key] = node 

      #Reset the minimum frequency to 1
      self.minFreq = 1
      self.insertAtHead(node, 1)

lfu = LFUCache(2)
lfu.put(1, 1)
lfu.put(2, 2)
print(lfu.get(1))
lfu.put(3, 3)
print(lfu.get(2))
print(lfu.get(3))
lfu.put(4, 4)
print(lfu.get(1))
print(lfu.get(3))
print(lfu.get(4))

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)