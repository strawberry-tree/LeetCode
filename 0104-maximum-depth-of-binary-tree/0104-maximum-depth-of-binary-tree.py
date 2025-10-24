# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        answer = 1

        while queue:
            curr, curr_depth = queue.popleft()
            answer = max(curr_depth, answer)
            if curr.left:
                queue.append((curr.left, curr_depth + 1))
            if curr.right:
                queue.append((curr.right, curr_depth + 1))

        return answer
        

