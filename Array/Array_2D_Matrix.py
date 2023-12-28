
# -----------------1D array by taking user input ---------------

# arr = []
# print("Enter the number: ")
# n = int(input())
# for i in range(n):
#     arr.append(int(input()))

# print("Data is: ")
# for j in range(n):
#     print(arr[j], end=" ")

# ----------------2D Arrray by taking user input and formation of Matrix---
from array import *
arr = []
print("Enter the dimensions:")
a = int(input("Rows: "))
b = int(input("Columns: "))

# Initialize the 2D array
print("Enter the data: ")
for i in range(a):
    # Append an empty list for each row
    arr.append([])
    for j in range(b):
        # Append elements to the current row
        arr[i].append(int(input()))

print("2D Array (Matrix):")
for i in range(0,a):
    for j in range(0,b):
        print(arr[i][j],end=' ')
    print()


    




























