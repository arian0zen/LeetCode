'''recursion with memory || O(mnN) || O(mnN)'''

def findPath(m, n , maxMove, startRow, startColumn):
    M = 1000000007
    N = maxMove
    hash_dp = {} #as we know there are multiple sybproblems, so we are not gonna solve all those! as we know, same sub problem will return same result,so we will store each solution, and later on when same problem occurs we will not calculate that, we will just return from out memory
    def recursion(m, n, i, j, N):
        if i == m or j == n or i < 0 or j < 0: #this is the base case, this is where ball goes out of boundaries, then we get one of our path
            return 1
        if N == 0: #when no more moves left, no where to go, return 0
            return 0
        if (m, n, i, j, N) in hash_dp: #if that same sub problem already exists, just return from memmory
            return hash_dp[(m, n, i, j, N)]
        else: #else, calculate that path and store in memory
            hash_dp[(m, n, i, j, N)] = recursion(m, n, i+1, j, N-1) + recursion(m, n, i-1, j, N-1) +recursion(m, n, i, j+1, N-1) + recursion(m, n, i, j-1, N-1)
            return hash_dp[(m, n, i, j, N)]
    return recursion(m, n, startRow, startColumn, maxMove) % M

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(findPath(m, n, maxMove, startRow, startColumn))

#instead of the hash_map we can also use an 3D array 
'''recursion with memory || O(mnN) || O(mnN)'''

def findPath(m, n , maxMove, startRow, startColumn):
    M = 1000000007
    N = maxMove
    dp = [[[-1]*(N+1) for _ in range(n+1)] for _ in range(m+1)] #as we know there are multiple sybproblems, so we are not gonna solve all those! as we know, same sub problem will return same result,so we will store each solution, and later on when same problem occurs we will not calculate that, we will just return from out memory
    # print(dp)
    def recursion(m, n, i, j, N):
        if i == m or j == n or i < 0 or j < 0: #this is the base case, this is where ball goes out of boundaries, then we get one of our path
            return 1
        if N == 0: #when no more moves left, no where to go, return 0
            return 0
        if dp[i][j][N] != -1:
            return dp[i][j][N] #if that same sub problem already exists, just return from memmory
            
        else: #else, calculate that path and store in memory
            dp[i][j][N] = recursion(m, n, i+1, j, N-1) + recursion(m, n, i-1, j, N-1) + recursion(m, n, i, j+1, N-1) + recursion(m, n, i, j-1, N-1)
            return dp[i][j][N]
    return recursion(m, n, startRow, startColumn, maxMove) % M

m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(findPath(m, n, maxMove, startRow, startColumn))



'''naive || recurse all the possible paths || O(4^n) as we have to make 4 choices at each stage'''
def findPaths(m, n , maxMove, startRow, startColumn):
    M = 1000000007
    if startRow == m or startColumn == n or startRow < 0 or startColumn < 0:
        return 1
    if maxMove <= 0:
           return 0
    return (findPaths(m, n, maxMove - 1, startRow -1, startColumn) +  findPaths(m, n, maxMove - 1, startRow +1, startColumn) +  findPaths(m, n, maxMove - 1, startRow, startColumn+1) +  findPaths(m, n, maxMove - 1, startRow, startColumn-1)) % M
    
    
    
    
m = 2
n = 2
maxMove = 2
startRow = 0
startColumn = 0
print(findPath(m, n, maxMove, startRow, startColumn))