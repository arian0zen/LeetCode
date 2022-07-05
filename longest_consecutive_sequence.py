def longestConsecutive(nums):
    nums = set(nums)
    longest_count = 0
    for i in nums:
        if i - 1 not in nums:
            max_count = 1
            current_nums = i
            while current_nums + 1 in nums:
                current_nums += 1
                max_count += 1
            longest_count = max(longest_count, max_count)
    return longest_count



nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))
#the logic
'''
This optimized algorithm contains only two changes from the brute force approach: the numbers are stored in a HashSet (or Set, in Python) to allow O(1)O(1) lookups, and we only attempt to build sequences from numbers that are not already part of a longer sequence. This is accomplished by first ensuring that the number that would immediately precede the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.
'''
        
        
#this approach takes O(n log n)  time complexity! but when the constraints are to apply the algorithm in O(n) we can choose the above approach
'''
    nums = set(nums)
    nums = list(nums)
    nums.sort()
    print(nums)
    if len(nums) == 0:
        return 0
    ans = 1
    max_count = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1]+1:
            ans += 1
        if nums[i] != nums[i-1]+1 :
            max_count = max(ans, max_count)
            ans  = 1
            # print (nums[i])
    return max(max_count, ans)
'''