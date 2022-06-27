def minDistance(word1, word2):
    n, m = len(word1), len(word2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for c in range(n+1):
        dp[0][c] = c
    for r in range(m+1):
        dp[r][0] = r
    # print (dp)
    for r in range(1, m+1):
        for c in range(1, n+1):
            if word1[c-1] == word2[r-1]:
                dp[r][c] = dp[r-1][c-1]
            else:
                insert = 1 + dp[r][c-1]
                delete = 1 + dp[r-1][c]
                replace = 1 + dp[r-1][c-1]
                dp[r][c] = min(insert, delete, replace)
                
    return dp[-1][-1]
    
    
    
    
print(minDistance("horsdse", "rods"))