# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(root):
        arr = []
        def traversal(root):
            if root == None: return
                #print("inside if")
               
           
            traversal(root.left)
            
            traversal(root.right)
            arr.append(root.val)
            
            #print (root.left.val)
        traversal(root)
        #print (arr)
        #print (len(set(arr)))
        if len(set(arr)) >=2:
            return False
        else:
            return True
        
    
    
#go to leet code to test the code with a proper treeNode input! thanks
        
        
        
        #second method
        
        
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        if(root.left != None):
            if(root.left.val != root.val):
                return False
        if(root.right != None):
            if(root.right.val != root.val):
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            

'''