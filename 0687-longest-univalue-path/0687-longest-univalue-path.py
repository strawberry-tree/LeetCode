# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    answer = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            left_path = dfs(node.left)
            right_path = dfs(node.right)
            print(node.val, left_path, right_path)

            flag1 = node.left and node.val == node.left.val
            flag2 = node.right and node.val == node.right.val

            if flag1 and flag2:
                self.answer = max(self.answer, left_path + right_path + 2)
                return max(left_path, right_path) + 1
            elif flag1:
                self.answer = max(self.answer, left_path + 1)
                return left_path + 1
            elif flag2:
                self.answer = max(self.answer, right_path + 1)
                return right_path + 1
            else:
                return 0

        dfs(root)
        return self.answer

           
        