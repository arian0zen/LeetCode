def searchRange(nums, target):
    ans1 = -1
    ans2 = -1
    n = len(nums)
    if len(nums)== 0:
        return ans1, ans2
        
    #binary search for left side (for the lower range) || when we read mid == target, we dont return, we search left side again to see if there are any lesser index with target value
        
    left = 0
    right = n - 1
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            ans1 = mid
            right = mid-1  
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
        
         
    #binary search for right side (for the upper range) || when we read mid == target, we dont return, we search left side again to see if there are any lesser index with target value
    left = 0
    right = n - 1 
    while left <= right:
        mid = (left+right) // 2
        if nums[mid] == target:
            ans2 = mid
            left = mid +1   
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid-1
            
            
    return ans1, ans2
    
    
nums = [5,7,7,8,8,10] 
target = 8   
print(searchRange(nums, target))