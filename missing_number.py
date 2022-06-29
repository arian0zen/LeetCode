def missingNumber(nums):
        
    if len(nums)==1 and nums[0]==0:
        return 1
    if len(nums)==1:
        return 0
    nums.sort()
        # print(nums)
    for i in range(0,len(nums)):
        if i != nums[i]:
            return i

    return len(nums)

print(missingNumber([3,0,1]))