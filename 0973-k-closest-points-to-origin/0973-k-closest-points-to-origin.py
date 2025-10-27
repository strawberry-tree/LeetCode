class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculate(x, y):
            return x ** 2 + y ** 2

        points.sort(key = lambda x: calculate(*x))
        return points[:k]