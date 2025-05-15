class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.oldest = Node(0, 0)
        self.latest = Node(0, 0)
        self.oldest.next = self.latest
        self.latest.prev = self.oldest

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.oldest.next
            self.remove(lru)
            del self.cache[lru.key]

    def remove(self, node: Node) -> None:
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def insert(self, node: Node) -> None:
        prev, next = self.latest.prev, self.latest
        next.prev = node
        prev.next = node
        node.next = next
        node.prev = prev


if __name__ == "__main__":
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    print(lRUCache.get(1))  # return 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(lRUCache.get(2))  # returns -1 (not found)
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(lRUCache.get(1))  # return -1 (not found)
    print(lRUCache.get(3))  # return 3
    print(lRUCache.get(4))  # return 4
