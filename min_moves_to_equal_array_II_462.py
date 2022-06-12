from array import array


# n = input("Enter the length of the array: ")
# array = []
# for i in range(int (n)):
#     elem = int(input("Enter the elements of the array: "))
#     array.append(elem)


array = [1,10,2,9]

array.sort()
#print(array)
n = len(array)
mid = n//2
#print(array[mid])   
count = 0
for element in range(n):
    
    if array[element] <= array[mid]:
        count += array[mid] - array[element]
    
    else:
        count += array[element] - array[mid]
    
print(count)