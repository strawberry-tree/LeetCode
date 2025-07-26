# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
from collections import defaultdict

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        dists = defaultdict(int)
        queue = deque([(root, 0)])

        while queue:
            curr, c_dist = queue.popleft()
            dists[c_dist] = curr.val
            if curr.left:
                queue.append((curr.left, c_dist + 1))
            if curr.right:
                queue.append((curr.right, c_dist + 1))

        results = []

        for value in dists.values():
            results.append(value)

        return results

        