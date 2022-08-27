def getRow(rowIndex):
    pascal = [[1]*i for i in range(1, rowIndex+2)]
    for i in range(2, rowIndex+1):
        for j in range(1, len(pascal[i])-1):
            pascal[i][j]= pascal[i-1][j-1]+pascal[i-1][j]
    return pascal[rowIndex]


rowIndex = 45
print(getRow(rowIndex))