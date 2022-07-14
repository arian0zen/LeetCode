def threeSum(nums, target):
        nums.sort()
        res = set()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: #this line to get check if we are checking duplicates! if duplicates found, simply skip that iteration
                continue
            target2 = target - nums[i]
            j = i+1
            right = n -1
            while j < right:
                sum_now = nums[j] + nums[right]
                if sum_now < target2:
                    j += 1
                elif sum_now > target2:
                    right -= 1
                else:
                    res.add((nums[i],nums[j],nums[right]))
                    j += 1
                    while j < right and nums[j] == nums[j-1]:
                        j += 1
        return res
    
nums = [-1,0,1,2,-1,-4]
target = 3 
print(threeSum(nums, target))
            