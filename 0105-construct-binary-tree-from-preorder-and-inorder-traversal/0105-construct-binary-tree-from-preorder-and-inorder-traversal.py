# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if len(inorder) < 1:
            return None

        for idx in range(len(preorder)):
            if preorder[idx] in inorder:
                root = preorder[idx]
                break

        inorder_idx = inorder.index(root)
        
        left = self.buildTree(preorder, inorder[:inorder_idx])
        right = self.buildTree(preorder, inorder[inorder_idx + 1:])
        
        new_root = TreeNode(val=root)
        new_root.left = left
        new_root.right = right
        return new_root