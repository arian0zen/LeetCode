
def firstMissingPositive(nums):
    nums.sort()
    a = 0
    for i in nums:
        if i > 0 :
            a = nums.index(i)
            break
        
    del nums[0:a]
    nums.insert(0, 0)
    nums = set(nums)
    nums = list(nums)

    if min(nums) > 1:
        return 1
    else:
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)
            
print(firstMissingPositive([7,1,4,-8]))