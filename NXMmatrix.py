from typing import List

def setZeros(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()
    
    # Step 1: Find all rows and columns that contain 0
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    
    # Step 2: Set the respective rows and columns to 0
    for r in zero_rows:
        for c in range(cols):
            matrix[r][c] = 0
    
    for c in zero_cols:
        for r in range(rows):
            matrix[r][c] = 0

# Example usage:
matrix1 = [
    [7, 19, 3],
    [4, 21, 0]
]

matrix2 = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 8, 9]
]

setZeros(matrix1)
setZeros(matrix2)

print(matrix1)  # Output: [[7, 19, 0], [0, 0, 0]]
print(matrix2)  # Output: [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
