# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def rec_invert(node):
            if node is None:
                return None
            node.left, node.right = rec_invert(node.right), rec_invert(node.left)
            return node

        return rec_invert(root)
        

        