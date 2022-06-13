from array import array
from webbrowser import get
import math

def partition(arr, l, r, ):
    #print (arr
    	
    x = arr[r]
    i = l
    #print (i)
    for j in range(l, r):
        #print (j)
            
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i]
            #print (arr[i], "->", arr[j])
            i += 1
            #print (i)
                
    arr[i], arr[r] = arr[r], arr[i]
    #print (arr[i])
    #print (arr[i])
    #print (arr[i])
    return i
            
def getmidelement(arr, l, r, mid):
    #print("in process of getting mid element")
    if(mid>0 and mid <= r-l +1 ):
        pivot_index = partition(arr, l, r)
        if pivot_index - l == mid -1:
           return arr[pivot_index]
        if pivot_index - l > mid -1:
            return getmidelement(arr, l, pivot_index-1, mid)
        return getmidelement(arr, pivot_index+1, r, mid-pivot_index+l-1)
    print ("not found")

arr = [7,10,4,3]
n = len(arr)
#print (n)
mid = math.ceil(n/2)
#print (mid)
#partition(arr, 0, n - 1)
mid_value = getmidelement(arr, 0, n-1, mid )
#print(mid_value)
a = mid_value
#print(a)
count = 0
for element in range(n):
    if (arr[element] <= mid_value):
        count += mid_value - arr[element]
    
    else:
        count += arr[element] - mid_value
    
print(count)

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