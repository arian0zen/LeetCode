def maxSatisfied(customers, grumpy, minutes):
    m = minutes
    sum = 0
    for each in range(len(customers)):
        if (grumpy[each] == 0):
            sum += customers[each]
        
    #print(sum)
    
    satisfaction = sum
    #setting up start and end pointers for the next loop
    start = 0
    end = start + m -1
    tempSum = 0 # this tempSum is only sum of first m customers when grumpy is 1
    
    for i in range(end+1):
        print("hi",i)
        # print(start, end)
        # print("ehehhe",i, grumpy[i])
        #print (i)
        if grumpy[i] == 1:
            #print(customers[i])
            tempSum = tempSum + customers[i]
        
            #print(start, end)
            
    #print(tempSum)
    start += 1
    end += 1
    maxSum = tempSum
    
    while end < len(customers):
        if grumpy[start-1] == 1:
            tempSum = tempSum - customers[start-1]
        if grumpy[end] == 1:
            tempSum = tempSum + customers[end]
    
        maxSum = max(maxSum, tempSum)
        start += 1
        end += 1
    
    return (satisfaction + maxSum)
            
    
    
       
print(maxSatisfied([2],[1],1))
        
        
