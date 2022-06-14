from array import array
from webbrowser import get
import math
import random



def partition(arr, l, r):
        random_i = random.randint(l, r)
        arr[l], arr[random_i] = arr[random_i], arr[l]
        pivot, j = arr[l], l
        for i in range(l + 1, r + 1):
            if arr[i] < pivot:
                j += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[l], arr[j] = arr[j], arr[l]
        return j
        

def getmidelement(arr, l, r, mid):
        #print("in process of getting mid element")
    if(mid>0 and mid <= r-l +1 ):
        pivot_index = partition(arr, l, r)
        if pivot_index - l == mid -1:
           return arr[pivot_index]
        if pivot_index - l > mid -1:
            return getmidelement(arr, l, pivot_index-1, mid)
        return getmidelement(arr, pivot_index+1, r, mid-pivot_index+l-1)
    return None


arr = [7,10,4,3]
n = len(arr)
mid = math.ceil(n/2)
mid_value = getmidelement(arr, 0, n-1, mid)

count = 0
for element in range(n):
    if (arr[element] <= mid_value):
        count += mid_value - arr[element]
    
    else:
        count += arr[element] - mid_value
    
print(count)


#print (mid_value)
#print (n)
#print (mid)
#partition(arr, 0, n - 1)
# mid_value = partition(arr, 0, n - 1)
# print(arr[mid_value])
#a = mid_value
#print(a)
# count = 0
# for element in range(n):
#     if (arr[element] <= mid_value):
#         count += mid_value - arr[element]
    
#     else:
#         count += arr[element] - mid_value
    
# print(count)
    # n = len(nums)
    # l, r, median_index = 0, n - 1, n >> 1
        
    # while True:
    #     index = partition(nums, l, r)
    #     if index < median_index:
    #         l = index + 1
    #     elif index > median_index:
    #         r = index - 1
    #     else:
    #         break
        
    #     return sum(abs(num - nums[median_index]) for num in nums)
            
# def getmidelement(arr, l, r, mid):
#     #print("in process of getting mid element")
#     if(mid>0 and mid <= r-l +1 ):
#         pivot_index = partition(arr, l, r)
#         if pivot_index - l == mid -1:
#            return arr[pivot_index]
#         if pivot_index - l > mid -1:
#             return getmidelement(arr, l, pivot_index-1, mid)
#         return getmidelement(arr, pivot_index+1, r, mid-pivot_index+l-1)
#     print ("not found")


# array.sort()
# #print(array)
# n = len(array)
# mid = n//2
# #print(array[mid])   
# count = 0
# for element in range(n):
    
#     if array[element] <= array[mid]:
#         count += array[mid] - array[element]
    
#     else:
#         count += array[element] - array[mid]
    
# print(count)

'''

def minMoves2(self, nums: List[int]) -> int:
        def partition(arr, l, r):
            random_i = random.randint(l, r)
            arr[l], arr[random_i] = arr[random_i], arr[l]
            pivot, j = arr[l], l
            for i in range(l + 1, r + 1):
                if arr[i] < pivot:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[j] = arr[j], arr[l]
            return j
        
        n = len(nums)
        l, r, median_index = 0, n - 1, n >> 1
        
        while True:
            index = partition(nums, l, r)
            if index < median_index:
                l = index + 1
            elif index > median_index:
                r = index - 1
            else:
                break
        
        return sum(abs(num - nums[median_index]) for num in nums)

'''