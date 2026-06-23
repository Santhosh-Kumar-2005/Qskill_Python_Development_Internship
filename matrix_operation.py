import numpy as np

def matrix_operations():
    print("Matrix Operations Tool")
    
    # Input matrices
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    
    print("\nMatrix A:\n", A)
    print("Matrix B:\n", B)
    
    # Addition
    print("\nA + B:\n", A + B)
    
    # Subtraction
    print("\nA - B:\n", A - B)
    
    # Multiplication
    print("\nA x B:\n", np.dot(A, B))
    
    # Transpose
    print("\nTranspose of A:\n", A.T)
    
    # Determinant
    print("\nDeterminant of A:", np.linalg.det(A))
    print("Determinant of B:", np.linalg.det(B))

# Run the tool
matrix_operations()
