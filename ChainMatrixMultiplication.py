def mcm(d):
    
    n = len(d)-1
    m = {(i,j):float('inf') for i in range(1,n+1) for j in range(1,n+1)}
    
    for i in range(1,n+1):
        m[(i,i)] = 0
        
    for i in range(1,n+1):
        for j in range(i,n+1):
            if i==j:
                m[(i,i)] = 0
            else:
                m[(i,j)] = min(m[(i,k)]+m[(k+1,j)]+(d[i-1]*d[k]*d[j]) for k in range(i,j))
    
    return m[(1,n)]


print(mcm([1,8,6,9]))
