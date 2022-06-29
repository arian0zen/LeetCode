
def firstMissingPositive(nums):
    if len(nums) == 1 and nums[0] >1:
        return 1
    if len(nums) == 1 and nums[0] >= 0:
        return nums[0]+1
    if len(nums) == 1 and nums[0] <0:
        return 1
    arr_pos = []
    for i in range(len(nums)):
        if nums[i] >= 0 :
            arr_pos.append(nums[i])
    arr_pos.append(0)
    arr_pos = set(arr_pos)
    arr_pos = list(arr_pos)
    arr_pos.sort()
    print(arr_pos)
    if min(arr_pos) > 1:
        return 1
    else:
        for i in range(len(arr_pos)):
            if i != arr_pos[i]:
                return i
        return len(arr_pos)
            
print(firstMissingPositive([7,1,4,-8]))