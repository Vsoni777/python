matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])
matrix.append([10,11,12])
print(matrix)
for row in matrix:
    for element in row:
        print(element,end=" ")