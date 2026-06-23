import numpy as np

print("MATRIX OPERATIONS TOOL")

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("\nEnter Matrix A")

A = []

for i in range(rows):
    row = list(map(int, input().split()))
    A.append(row)

A = np.array(A)

print("\nEnter Matrix B")

B = []

for i in range(rows):
    row = list(map(int, input().split()))
    B.append(row)

B = np.array(B)

while True:

    print("\n----- MENU -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("\nAddition")
        print(A + B)

    elif choice == 2:
        print("\nSubtraction")
        print(A - B)

    elif choice == 3:
        print("\nMultiplication")
        print(np.dot(A, B))

    elif choice == 4:
        print("\nTranspose of Matrix A")
        print(A.T)

    elif choice == 5:

        if rows == cols:
            print("\nDeterminant of Matrix A")
            print(np.linalg.det(A))
        else:
            print("Determinant only for square matrices")

    elif choice == 6:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
