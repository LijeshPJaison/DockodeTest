m = int(input("Enter the number of rows:"))
n = int(input("Enter the number of columns:"))
matrix = [[0 for x in range(n)] for y in range(m)]

counter = 1

for k in range(n+m-1):
    for j in range(k+1):
        i = k-j

        if(i < m and j < n):
            matrix[i][j] = counter
            counter += 1

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()