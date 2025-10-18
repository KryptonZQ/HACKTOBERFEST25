
rows, cols = map(int, input("Enter number of rows and columns: ").split())

matrix = []
print("Enter matrix elements row-wise:")
for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

# Display the matrix
print("\nMatrix:")
for row in matrix:
    print(*row)

# Sum of each row
print("\nSum of each row:")
for i in range(rows):
    row_sum = sum(matrix[i])
    print(f"Row {i+1}: {row_sum}")

# Sum of each column
print("\nSum of each column:")
for j in range(cols):
    col_sum = sum(matrix[i][j] for i in range(rows))
    print(f"Col {j+1}: {col_sum}")

# Maximum element in the matrix
max_element = max(max(row) for row in matrix)
print(f"\nMaximum element: {max_element}")