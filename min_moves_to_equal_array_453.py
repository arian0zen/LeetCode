from array import array


# n = input("Enter the length of the array: ")
# array = []
# for i in range(int (n)):
#     elem = int(input("Enter the elements of the array: "))
#     array.append(elem)


array = [1, 2, 3]

n = len(array)
    
#print (array)

min_array = min(array)

#print (min_array)

# for each in array:
count = 0

sum_array = sum(array)

count = sum_array - n*min_array  #this is the formula!! the math and approach written in pioneer 160pages (space_red)

print (count)
    
    