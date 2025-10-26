class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.q = [None] * k
        self.front = 0  # 맨 앞
        self.back = 0   # 맨 뒤 + 1
        self.items = 0
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.back] = value
        self.back = (self.back + 1) % self.size
        self.items += 1

        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        value = self.q[self.front]
        self.front = (self.front + 1) % self.size
        self.items -= 1
        return True
        

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.front]
        

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.back - 1]
        

    def isEmpty(self) -> bool:
        return self.items <= 0
        

    def isFull(self) -> bool:
        return self.items >= self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()