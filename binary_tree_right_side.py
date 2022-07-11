# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
#         ans = []
#         if root == None:
#             return ans
#         queue = []
#         queue.append(root)
#         while len(queue) > 0:
#             right_side = None
#             n = len(queue)
#             for node in range(n):
#                 node = queue.pop(0)
#                 if node != None:
#                     right_side = node
#                     queue.append(node.left)
#                     queue.append(node.right)
#             if right_side != None:
#                 ans.append(right_side.val)
#         return ans
                    
                