# from array import *
arr = []
print("Enter the dimensions:")
a = int(input("Rows: "))
b = int(input("Columns: "))

# -----------------------Steps of taking user input in 2-D Array----------

# Initialize the 2D array
print("Enter the data: ")
for i in range(a):
    # Append an empty list for each row
    arr.append([])
    for j in range(b):
        # Append elements to the current row
        arr[i].append(int(input()))

# -----------------------------------***********----------------------------
print("2D Array (Matrix):") 
for i in range(0,a):
    for j in range(0,b):
        print(arr[i][j],end=' ')
    print()

print("Sum and Transopose of the (Matrix):")
sum = 0
for i in range(0,a):
    for j in range(0,b):
        print(arr[j][i],end=' ')
        sum = sum + arr[j][i]
    print()

print("Sum is: ", sum)



    




























