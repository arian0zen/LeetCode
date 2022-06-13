'''
just the driver code
'''

class Solution(object):
    def kthSmallest(self, root, k):
        self.arr = []
        #print(root.val)
        def inOrderTraversal(root):
            if root == None: return
            
            inOrderTraversal(root.left)
            #print("left:",root.val)
            self.arr.append(root.val)
            inOrderTraversal(root.right)
            # print (root.val)
            # print  (root.right)
            #print ("right:", root.val)
            #self.arr.append(root.val)
            
            # self.arr.append(root.val)
            
        inOrderTraversal(root)
        return self.arr[k - 1]
        #print (self.arr)
        
        
#print all the commented code and you will get a better understanding of what the code is doing