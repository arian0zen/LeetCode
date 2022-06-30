def findDisappearedNumbers(nums):
    hash_dict = {i: 0 for i in range(1,len(nums)+1)}
        
    for i in range(len(nums)):
           hash_dict[nums[i]] += 1
        
    ab = []
    for i in range(1, len(nums)+1):
        if hash_dict[i] ==  0:
            ab.append(i)
    return ab


print(findDisappearedNumbers([4,3,2,7,8,2,3,1]))






# a = []          
# for i in range(len(hash_dict)):
#     if hash_dict[i] == 0:
#         a.append(i)
    
# print (len(hash_dict) + 1)
    


# class Solution:
#     def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
#         nums = set(nums)
#         nums = list(nums)
#         n = len(nums)
#         b =[]
#         a = [1]
#         if len(nums) == 1 and nums[0] == 1:
#             nums[0] = 2
#             return nums
#         if min(nums) > 1:
#             return a
#         sum_og = (n*(n+1))//2
#         sum_now = sum(nums)
#         sum_diff = abs(sum_og - sum_now)
#         missed_nums = abs(n - max(nums))
#         a = 0
#         for i in range(len(nums)):
#             if i != nums[i]:
#                 a = i
#         array= []
#         sum_a = 0
#         for i in range(missed_nums):
#             if sum_a != sum_diff:
#                 array.append(a+i)
#                 sum_a += (a+i)
#         return array
        