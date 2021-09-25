def LCW(A,B):
    n = len(A)
    m = len(B)

    #Initializing first row and column with 0 (for ease i intialized everthing 0 :p)
    dp = [[0]*(m+1) for _ in range(n + 1)]

    final = 0

    #this code is a lot like longest common subsequence(only else condition is different). 
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:
                dp[i][j] = 0

            final = max(final, dp[i][j])

    return final

print(LCW("director","secretary"))
