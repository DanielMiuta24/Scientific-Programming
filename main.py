# importing libraries
import numpy as np

def number_to_string(argument):
    match argument:
        case 1:
            return "Addition"
        case 2:
            return "Subtraction"
        case 3:
            return "Multiplication"
        case 4:
            return "Transpose"
        case default:
            return "Invalid Selection"

def input_matrix(rows, columns):
    matrix = []
    print(f"Enter the entries for a {rows}x{columns} matrix row wise:")
    for row in range(rows):
        a = []
        for column in range(columns):
            a.append(int(input()))
        matrix.append(a)
    return np.array(matrix)

def matrix_operations(matrixA, matrixB, operation):
    if operation == 1:  # Addition
        if matrixA.shape == matrixB.shape:
            return matrixA + matrixB
        else:
            print("Addition not possible. Matrices must have the same dimensions.")
            return None
    elif operation == 2:  # Subtraction
        if matrixA.shape == matrixB.shape:
            return matrixA - matrixB
        else:
            print("Subtraction not possible. Matrices must have the same dimensions.")
            return None
    elif operation == 3:  # Multiplication
        if matrixA.shape[1] == matrixB.shape[0]:
            return np.dot(matrixA, matrixB)
        else:
            print("Multiplication not possible. Number of columns in A must equal number of rows in B.")
            return None
    elif operation == 4:  # Transpose
        return matrixA.T
    else:
        print("Invalid operation!")
        return None

# Get matrix dimensions and inputs for matrix A
RowA = int(input("Enter the number of rows for the first matrix: "))
ColumnA = int(input("Enter the number of columns for the first matrix: "))
matrixA = input_matrix(RowA, ColumnA)

# Get matrix dimensions and inputs for matrix B
RowB = int(input("Enter the number of rows for the second matrix: "))
ColumnB = int(input("Enter the number of columns for the second matrix: "))
matrixB = input_matrix(RowB, ColumnB)

# Display the matrices and their dimensions
print("\nMatrix A:")
print(matrixA)
print('Dimensions of Matrix A: ', matrixA.shape)

print("\nMatrix B:")
print(matrixB)
print('Dimensions of Matrix B: ', matrixB.shape)

# Display available operations
print('\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Transpose')
onPress = int(input('Input a number to perform an operation: '))

operation_name = number_to_string(onPress)
print(f'\nSelected Operation: {operation_name}')

# Perform the operation
if onPress == 4:  # Transpose operation only requires one matrix
    result = matrix_operations(matrixA, None, onPress)
    print("Result of Transpose of Matrix A:")
    print(result)
else:
    result = matrix_operations(matrixA, matrixB, onPress)
    if result is not None:
        print("Result:")
        print(result)
        # end