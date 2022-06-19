
def findCircleNum(matrix ):
        if matrix == [[]]:
            return "no island found"
        else:
            
            rows = len(matrix)
            columns = len(matrix[0])
            island = 0
          
        def checkValidIsland(r, c, rows, columns, matrix):
            if  (r>=0 and r < rows and
                c>=0 and c < columns and
                matrix[r][c] == 1):
                return True
            else: 
                return False 
        
        def dfs(r, c, rows, columns, matrix): 
                matrix[r][c] = 0 # mark as visited
               
                if checkValidIsland(r-1, c, rows, columns, matrix) == True:
                    dfs(r-1, c, rows, columns, matrix)
                    
                if checkValidIsland(r+1, c, rows, columns, matrix) == True:
                    dfs(r+1, c, rows, columns, matrix)
                
                if checkValidIsland(r, c-1, rows, columns, matrix) == True:
                    dfs(r, c-1, rows, columns, matrix)
                    
                if checkValidIsland(r, c+1, rows, columns, matrix) == True:
                    dfs(r, c+1, rows, columns, matrix)
                
        
        for r in range(rows):
            for c in range(columns): 
                if matrix[r][c] == 1 :
                    island = island + 1
                    dfs(r,c, rows, columns, matrix)
                    
                    
                    
        #print(matrix) 
        return island
    
print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))
        