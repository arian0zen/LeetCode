''''You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get
Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.'''

def maxResult(nums, k):
    start = 0
    sum = nums[0]
    print (nums[start+1:start+k+1])
    for i in range(len(nums)):
        print(start)
        if start == len(nums) - 1:
            break
        elif start+k+1 <= len(nums)-1:
            temp = (max(nums[start+1:start+k+1]))
            start = nums.index(temp)
            sum += temp
        elif start+k+1 >= len(nums)-1:
            temp = (max(nums[start+1:len(nums)]))
            start = nums.index(temp)
            sum += temp
            
    return(sum)
        
        
        
    
    
    
    

nums = [100,-1,-100,-1,100]
k = 2
print(maxResult(nums, k))
