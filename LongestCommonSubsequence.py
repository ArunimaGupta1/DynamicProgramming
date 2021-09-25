def LCS(u,v):
    m = len(u)
    n = len(v)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(1,m+1):
        for j in range(1,n+1):
            if u[i-1]==v[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                
    return(dp[m][n])


print(LCS("director","secretary"))
