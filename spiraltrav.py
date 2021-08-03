def generate(n):
    k = 0 #row1
    l = 0 #col1
    m = n #row2
    nc = n#col2
    mat = [ [0 for i in range(n)] for j in range(n)]
    num = 1
    while (k < m and l < n) : 
        
        for i in range(l, n) : 
           mat[k][i] = num 
           num+=1
        
        k += 1

      
        for i in range(k, m) : 
            mat[i][n - 1]=num
            num+=1

        n -= 1

        if ( k < m) : 

            for i in range(n - 1, (l - 1), -1) : 
                mat[m - 1][i] = num 
                num+=1

            m -= 1

        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                mat[i][l] = num 
                num+=1

            l += 1
    return mat
            
if __name__ == "__main__":
    n = int(input())
    print(generate(n))