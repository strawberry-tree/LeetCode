class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        def searchArea(up, down, left, right): 
            if up > down or left > right:
                return False

            row_mid = (up + down) // 2
            col_mid = (left + right) // 2
            curr = matrix[row_mid][col_mid]

            if target == curr:
                return True
            elif curr < target:
                s1 = searchArea(up, down, col_mid + 1, right)
                s2 = searchArea(row_mid + 1, down, left, right)
                return s1 or s2
            elif target < curr:
                s1 = searchArea(up, down, left, col_mid - 1)
                s2 = searchArea(up, row_mid - 1, left, right)
                return s1 or s2

        return searchArea(up, down, left, right)
            