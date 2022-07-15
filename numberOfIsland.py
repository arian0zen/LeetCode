import collections
from itertools import count
from nntplib import GroupInfo


class Solution:
    def numIslands(matrix: list[list[str]] ):
        
        if matrix == [[]]:
            return "no island found"
        else:
            #print ("inside else")
            rows = len(matrix)
            columns = len(matrix[0])
            island = 0
            
            #print(columns, rows)
            #print (visited)
            #print (rows, columns)
            
        
        '''
        def bfs(r, c):
            if (r, c) not in visited:
            #print ("inside bfs")
            #queued = collections.deque()
                visited.append((r,c))
            #queued.append((r,c))
            #print (visited)
            #print (queued)
            #while queued:
                #row, column = queued.popleft()
                #print (row, column)
                directions = [[-1, 0], [1,0], [0,1], [0,-1]]
                for  rw, cl in directions:
                    #print (rw, cl)
                    r = row + rw
                    c = column + cl
                    #print (c, r)
                    if(r >= 0 and r < rows and
                       c >= 0 and c < columns and
                       matrix[r][c] == '1' and
                       (r,c) not in visited):
                        #print ("inside bfs if")
                        
                        queued.append((r,c))
                        visited.append((r,c,))
                        #print (visited)
                        '''
                        
        def checkValidIsland(r, c, rows, columns, matrix): #r and c is co ordinate of the matrix as 00, 01, 02......
            if  (r>=0 and r < rows and
                c>=0 and c < columns and
                matrix[r][c] == 1):
                return True
            else: 
                return False
                
                        
        max_counter = 0   
        def dfs(r, c, rows, columns, matrix): #this is actually BFS call, i am stupid lol
                matrix[r][c] = 0 #marking that co ordinate as 0 so we don't visit it again
                #print (r,c) #uncomment this to see the r and c of the matrix
                nonlocal counter
                counter += 1
               
                if checkValidIsland(r-1, c, rows, columns, matrix) == True: #this is the recursion base case
                    dfs(r-1, c, rows, columns, matrix)
                    
                if checkValidIsland(r+1, c, rows, columns, matrix) == True:
                    dfs(r+1, c, rows, columns, matrix)
                
                if checkValidIsland(r, c-1, rows, columns, matrix) == True:
                    dfs(r, c-1, rows, columns, matrix)
                    
                if checkValidIsland(r, c+1, rows, columns, matrix) == True:
                    dfs(r, c+1, rows, columns, matrix)
                    
                '''
                else:
                    return False
                    '''
                
                
                
        
        for r in range(rows):
           
            for c in range(columns):
                
                if matrix[r][c] == 1 :
                    island = island + 1
                    
                    
                    #bfs(r, c)
                    #print ("The count of islands is: ", island, r, c)
                    
                    counter = 0
                    dfs(r,c, rows, columns, matrix)
                    print(counter)
                    max_counter = max(max_counter, counter)
                    
                    
                    
        print(matrix) 
        print ("isnland: ", island, max_counter)
    
    
    matrix= [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    
    '''
    [ 
            [0,1,1, 0, 1],
            [1,1,0, 1,1],
            [1,0,0, 1,0],
            [1,0,1, 0,1],
            [1,1,0, 0,0],
            [1,1,0, 0,0]]
            
            
            
             [  [1,1,1,1,1,1,1,1,1,1],
            [1,1,0,1,1,0,1,1,0,1],
            [1,1,1,1,1,1,1,1,1,1]]
    '''

    numIslands(matrix)
                                    