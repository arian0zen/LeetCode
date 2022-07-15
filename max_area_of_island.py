#this one is the same problem as the number of islands
#there we needed to find how many distinct islands are there
#in this one we gotta get which one of those island is largest
#what i did is when ever i visit a 1..i keep a count! and then another max_count keeps track of which among those are max (largest)
def maxAreaOfIsland(matrix):
    if matrix == [[]]:
        return "no island found"
    else:
        #print ("inside else")
        rows = len(matrix)
        columns = len(matrix[0])
        island = 0
            
        
    def checkValidIsland(r, c, rows, columns, matrix): #r and c is co ordinate of the matrix as 00, 01, 02......
        if  (r>=0 and r < rows and
            c>=0 and c < columns and
            matrix[r][c] == 1):
            return True
        else: 
            return False
                
        
            
    def dfs(r, c, rows, columns, matrix):
            #this is actually BFS call, i am stupid lol
            matrix[r][c] = 0 #marking that co ordinate as 0 so we don't visit it again
            #print (r,c) #uncomment this to see the r and c of the matrix
            nonlocal counter
            counter += 1
                
                
               
            if checkValidIsland(r-1, c, rows, columns, matrix) == True:
                dfs(r-1, c, rows, columns, matrix)
                    
            if checkValidIsland(r+1, c, rows, columns, matrix) == True:
                dfs(r+1, c, rows, columns, matrix)
                
            if checkValidIsland(r, c-1, rows, columns, matrix) == True:
                dfs(r, c-1, rows, columns, matrix)
                    
            if checkValidIsland(r, c+1, rows, columns, matrix) == True:
                dfs(r, c+1, rows, columns, matrix)
                    
    max_count = 0
        
    for r in range(rows):
           
        for c in range(columns):
                
            if matrix[r][c] == 1 :
                island = island + 1
                    
                counter= 0
                dfs(r,c, rows, columns, matrix)
                max_count = max(counter, max_count)

    return max_count #also the island variable stores how many island found
        
        
matrix = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(matrix))