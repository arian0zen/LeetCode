def maximumUnits(boxTypes, truckSize):
    boxTypes.sort(key=lambda x: x[1], reverse = True)
    ans = 0
    for i in range (len(boxTypes)):
            
        if boxTypes[i][0] <= truckSize:
                
            truckSize -= boxTypes[i][0]
                
            ans += (boxTypes[i][0]) * boxTypes[i][1]
            
        elif boxTypes[i][0] > truckSize:
                
            ans += truckSize * boxTypes[i][1]
                
            truckSize -= truckSize
                
    return ans


boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
print(maximumUnits(boxTypes, truckSize))