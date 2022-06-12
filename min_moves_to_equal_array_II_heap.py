from array import array
import heapq

# n = input("Enter the length of the array: ")
# array = []
# for i in range(int (n)):
#     elem = int(input("Enter the elements of the array: "))
#     array.append(elem)


#array = [1,10,2,9]


array =[-74, 0, -4, 20, 7, 1, -4700, 74, 21, 71000, 87, 400, 9]
# print ("The array: ", array)
# print("")
heapArray = array
length = len(array)
heapq.heapify(heapArray)
sortedArray = []

for each in (array[:length]):
    sortedArray.append(heapq.heappop(heapArray))
    
array = sortedArray
#print ("The sorted array is:", array)



#array.sort()
#print(array)
#n = len(array)
mid = length//2
#print(array[mid])   
count = 0
for element in range(length):
    
    if array[element] <= array[mid]:
        count += array[mid] - array[element]
    
    else:
        count += array[element] - array[mid]
    
print(count)
        