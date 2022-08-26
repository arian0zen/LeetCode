
def canJump(nums):
    n = len(nums)
    dp = [0]*n
    dp[0] = nums[0]
    for i in range(1, n):
        if dp[i-1] <= 0:
            return False
        dp[i] = max(dp[i-1]-1, nums[i])
            
    return True

nums = [2,3,1,1,4]
print(canJump(nums))