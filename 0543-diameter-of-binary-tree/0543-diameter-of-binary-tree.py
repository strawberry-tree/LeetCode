# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                # 루트가 지금 노드인 트리의 직경 / leaf로부터 현재노드 깊이
                return 0, 0
            l_dia, l_depth = dfs(node.left)
            r_dia, r_depth = dfs(node.right)
            sum_depths = l_depth + r_depth

            diameter = max(l_dia, r_dia, sum_depths)
            depth = max(l_depth, r_depth) + 1
            return diameter, depth

        return dfs(root)[0]

        
            
        