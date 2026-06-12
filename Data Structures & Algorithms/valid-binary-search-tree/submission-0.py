# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float("-inf"), float("inf"))
    def validate(self, node, p, q):
        if not node:
            return True
        
        if p >= node.val or q <= node.val:
            return False
        
        return self.validate(node.left, p, node.val) and self.validate(node.right, node.val, q)