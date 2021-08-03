def sol(mat,n):
    for row in range(n):
        for col in range(row,n):
            mat[row][col],mat[col][row] = mar[col][row],mat[row][col]
    
    for row in mat:
        row = row.reverse()
    print(mat)





if __name__ == "__main__":
    test = int(input())
    for cases in range(test):
        n = int(input())
        mat = []
        for i in range(n):
            l = list(map(int,input().split()))
            mat.append(l)
        sol(mat,n)