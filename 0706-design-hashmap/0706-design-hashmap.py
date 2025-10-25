class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.table = [None] * 1000
    
    def hash(self, key: int) -> int:
        return key % 1000

    def put(self, key: int, value: int) -> None:
        idx = self.hash(key)
        node = self.table[idx]

        if node is None:
            self.table[idx] = ListNode(key = key, value=value)
        else:
            while node:
                # 이미 key가 존재
                if node.key == key:
                    node.value = value
                    return
                if node.next:
                    node = node.next
                else:
                    node.next = ListNode(key=key, value=value)
                    return


    def get(self, key: int) -> int:
        idx = self.hash(key)
        node = self.table[idx]
        
        while node:
            if node.key == key:
                return node.value
            node = node.next
        
        return -1
        
    def remove(self, key: int) -> None:
        idx = self.hash(key)
        node = self.table[idx]
        prev = None

        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.table[idx] = node.next
                return
            prev, node = node, node.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)