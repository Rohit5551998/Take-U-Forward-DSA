class Node: 
  def __init__(self, key: int, value: int):
    self.value = value
    self.key = key
    self.prev = None
    self.next = None

class LRUCache:
  def __init__(self, capacity: int):
    self.head = Node(-1, -1)
    self.tail = Node(-1, -1)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.map = {}
    self.capacity = capacity

  def deleteNode(self, node: Node):
    prevNode = node.prev
    nextNode = node.next
    prevNode.next = nextNode
    nextNode.prev = prevNode

  def insertAtHead(self, node: Node):
    nextNode = self.head.next
    self.head.next = node
    node.prev = self.head
    node.next = nextNode
    nextNode.prev = node

  def get(self, key: int) -> int:
    ans = -1
    if (key in self.map):
      node = self.map[key]
      ans = node.value
      self.deleteNode(node)
      self.insertAtHead(node)
    return ans
      

  def put(self, key: int, value: int) -> None:
    if (key in self.map):
      node = self.map[key]
      self.deleteNode(node)
      self.insertAtHead(node)
      node.value = value
    else:
      if (len(self.map.values()) == self.capacity):
        lruNode = self.tail.prev
        del self.map[lruNode.key]
        self.deleteNode(lruNode)
      node = Node(key, value)
      self.map[key] = node  
      self.insertAtHead(node)

lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))
lru.put(3, 3)
print(lru.get(2))
# lru.put(4, 4)
# print(lru.get(1))
# print(lru.get(3))
# print(lru.get(4))