# https://leetcode.com/problems/validate-binary-search-tree/submissions/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root) if root else True
    
    def dfs(self, node, lower = float('-inf'), upper = float('inf')):
        if not node:
            return True
        
        if node.val <= lower or node.val >= upper:
            return False
 
        return self.dfs(node.left, lower, node.val) and self.dfs(node.right, node.val, upper)