# So we follow a simple Intuition

# Either the node is a part of an existing Zig-Zag path, or a new Zig-Zag path begins from that node
# At each node we check the previous turn, and then progress accordingly
# We either continue in the same direction, or make a new path
# We update our answer, which is a global variable everytime we reach a NULL node.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# def longestZigZag(self, root: Optional[TreeNode]) -> int:
#         if root==None:
#             return 0
#         self.max = 1
        
        
#         def travel(prev,node,count):
#             if node==None:
#                 self.max = max(self.max,count)
#                 return
#             if prev=='right':
#                 travel('left',node.left,count+1)
#                 travel('right',node.right,1)
#             else:
#                 travel('right',node.right,count+1)
#                 travel('left',node.left,1)
        
        
#         travel('right',root.right, 1)
#         travel('left',root.left, 1)
#         return self.max-1