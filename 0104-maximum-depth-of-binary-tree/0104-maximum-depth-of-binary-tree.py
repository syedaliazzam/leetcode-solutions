# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, n: Optional[TreeNode]) -> int:
        return n and 1+max(self.maxDepth(n.left),self.maxDepth(n.right)) or 0