# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root) -> int:
        def dfs(root, max_node):
            if root == None:
                return 0
            count = 1 if root.val >= max_node else 0 
            max_node = max(max_node, root.val)
            count += dfs(root.left, max_node)
            count += dfs(root.right, max_node)
            return count
        return dfs(root, root.val)
            
            
#go to leet code for checking