# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # root 1 기준으로 합치기
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root1, root2):
            # root1, root2 모두 null인 경우
            if not root1 and not root2:
                return None
            
            # root2 값만 존재 -> 여기서부터 바로 서브트리 가져오기
            if not root1:
                return root2

            # root1 값만 존재 -> 여기서부턴 뭐 더 할게 없음
            if not root2:
                return root1
            
            # 두 값이 모두 존재
            root1.left = dfs(root1.left, root2.left)
            root1.right = dfs(root1.right, root2.right)
            root1.val += root2.val
            return root1
        
        return dfs(root1, root2)