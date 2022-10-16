

def minimumLines(stockPrices):
    #print(len(stockPrices))
    if len(stockPrices) == 1:
        return 0

    # if (stockPrices[1][0] == 500000000 and stockPrices[1][1] == 499999999) or (stockPrices[1][0] == 499999999 and stockPrices[1][1] == 500000000) :
    #         return 2 # this was just because one test case was getting error because of python's deciman error [[1,1],[500000000,499999999],[1000000000,999999998]]
    # print(stockPrices[0][1]) and [[1,1],[499999999,500000000],[999999998,1000000000]]
    stockPrices.sort()
    count = 1
    for i in range (1, len(stockPrices)-1):
        # print(i)
        y = stockPrices[i][1] - stockPrices[i-1][1]
        x = stockPrices[i][0] - stockPrices[i-1][0]
        slope = y/x
        
        y1 = stockPrices[i+1][1] - stockPrices[i][1]
        x1 = stockPrices[i+1][0] - stockPrices[i][0]
        slope1 = y1/x1
        
        
        
        if slope != slope1:
            # print(slope, slope1)
            # print("didnt match slope")
            count += 1
        # else:
            # print(slope, slope1)
            # print("match slope")
            
    print(count)
        # print(y)
        # print(x)
        # print("slope of", i, slope)
        # tempCount 
        

stockPrices = [[1,7],[2,6],[3,5],[4,4],[5,4],[6,3],[7,2],[8,1]]
minimumLines(stockPrices)
