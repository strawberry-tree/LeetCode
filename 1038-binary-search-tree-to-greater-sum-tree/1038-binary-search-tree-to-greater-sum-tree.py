# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 우측 -> 중간 -> 좌측 순으로 순회?
class Solution:
    cum_sum = 0
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return
        self.bstToGst(root.right)
        self.cum_sum += root.val
        root.val = self.cum_sum
        self.bstToGst(root.left)
        
        return root