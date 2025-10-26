class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.q = [None] * self.size
        self.front = 0
        self.back = 1
        self.items = 0
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.front] = value
        self.front = (self.front - 1) % self.size
        self.items += 1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.back] = value
        self.back = (self.back + 1) % self.size
        self.items += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.q[(self.front + 1) % self.size] = None
        self.front = (self.front + 1) % self.size
        self.items -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.q[(self.back - 1) % self.size] = None
        self.back = (self.back - 1) % self.size
        self.items -= 1
        return True
        

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.front + 1) % self.size]
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.back - 1) % self.size]
        

    def isEmpty(self) -> bool:
        return self.items == 0
        

    def isFull(self) -> bool:
        return self.items == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()