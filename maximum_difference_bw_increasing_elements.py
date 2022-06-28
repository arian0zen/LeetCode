

from calendar import different_locale

 #optimized i guess, time O(n)
def maximumDifference(nums):
    n = len(nums)
    min_prefix = nums[0]
    difference = -1
    for i in range(n):
        min_prefix = min(min_prefix, nums[i])
        if nums[i] > min_prefix and nums.index(min_prefix) < i :
            difference = max(difference, abs(min_prefix - nums[i]))
        
    return difference    

nums = [7,1,5,4]
print(maximumDifference(nums))    

 # return sum(nums) 
    # left = 0
    # right = 1
    # difference = -1
    # while left < len(nums) and right < len(nums):
    #     # print (nums[right])
    #     if nums[left] <= nums[right]:
    #         difference = max((nums[right] - nums[left]), difference)
    #         # print (difference)
    #         right += 1
    #     else:    
    #         right += 1
            
    #     left += 1
            
    # return difference
    
    # *** TRIED
    
    # min_nums = min(nums)
    # min_index = nums.index(min_nums)
    # n = len(nums)
    # print (min_index)
    # difference = -1
    # for i in range (n):
    #     if min_index >= 0 and i > 0 :
    #         difference = max(difference, (nums[i] - min_nums))
    #         print (difference)
    # return difference
    
    # *** TRIED
     #naivest fucking approach time O(n^2)
    # n = len(nums)
    # difference = -1
    # for i in range(n):
    #     for j in range(i+1,n):
    #         if nums[i] < nums[j]:
    #             difference = max(difference, (nums[j]-nums[i]))
    #             print ((nums[j],nums[i]), difference)            
    # return difference