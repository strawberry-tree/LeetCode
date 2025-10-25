# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0
            # 더 작은 쪽을 찾아보는 것은 무의미
            if node.val < low:
                return dfs(node.right)
            # 더 큰 쪽을 찾아보는 것은 무의미
            if high < node.val:
                return dfs(node.left)
            return node.val + dfs(node.right) + dfs(node.left)

        return dfs(root)