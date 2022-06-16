from cmath import e


*** TRIED SO HARD STILL DID NOT GET THE DESIRED OUT PUT IN O(n) TIME AND SPACE ***

#def containsNearbyDuplicate(arr, k, t):
    
#     n = len(arr)
#     print (n)
#     if n == 1 or n == None :
#         return False
#     aa = 0
    
#     for elements in range(len(arr)-k):
#         #print(elements, n)
#         if (abs(arr[elements] - arr[elements+k]) > t):
#             #print("this returned true for: ", arr[elements], arr[elements+k])
            
#             aa = 1
        
        
        
#     print(aa)
#     n = len(arr)
    
#     hash_dict ={}
#     if aa == 0:
#         for index, each in enumerate(arr):
#             if(abs(index - hash_dict[each]) <= k) :
#                 return True
#             hash_dict[each] = index
#         return False
     
    
# print(containsNearbyDuplicate([1,2,3,1], 3, 0))
# # hash_dict = {}
# # arr = [1,5,9,1,5,9]
# # for index, each in enumerate(arr):
# #         hash_dict[each] = index
        
# #         #print(each)    
# #         print(hash_dict.values)