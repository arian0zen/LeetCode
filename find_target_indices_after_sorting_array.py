
def targetIndices(nums, target) :
    nums.sort()
    ans = []
        
    for i in range(len(nums)):
        if nums[i] > target:
            break
        if nums[i]  == target:
            ans.append(i)
            
    return (ans)
                
           
nums = [1,2,5,2,3]
target = 5
print(targetIndices(nums, target))

#enumerate (from leet code, credim to them)
'''def targetIndices(nums, target) :
    ret = []
    nums.sort()
    for i in enumerate(nums):
        print (i)
        if i[1] == target:
            ret.append(i[0])
        
    return ret'''
                


#logically better approach;  (from leet code, credim to them)
'''
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target) == 0:
            return []
        nums = sorted(nums)
        idx = []
        for i in range(nums.index(target), len(nums)):
            if nums[i] == target:
                idx.append(i)
            else:
                break
        return idx
'''