from gettext import find


#simple enumerate iterating

def findMaxConsecutiveOnes(nums):
    
    max_one = 0
    count = 0    
    for i in nums:
        
        # print (i)
        if i == 1:
            count += 1
        elif i == 0:
            # print("inside elif")
            
            count = 0
        max_one = max(count, max_one)
    return max_one
 

nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))


#two pointers approach, sling window technique

# def findMaxConsecutiveOnes(self, nums):
#     # nums.append(0)
#     max_one = 0
#     count = 0    
#     low = 0
#     high = 0
#     i = 0
#     while high < len(nums):
#         if nums[i] == 1:
#             high += 1
#             count = high - low  
#         else: 
#             count = high - low
#             low = high+1
#             high += 1
            
#         max_one = max(count, max_one)
#         i = i+1
            
#     return max_one
        
