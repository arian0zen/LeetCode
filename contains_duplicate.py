import re


def containsDuplicate(nums):
    #print (len(set(nums)), len(list(nums)))
    # print (set(nums))
    # print(list(nums))
    if (len(set(nums)) == len(list(nums))):
        return False
    else:
        return True
    


print(containsDuplicate([1,2,3,1]))













'''

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 01:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true


'''
