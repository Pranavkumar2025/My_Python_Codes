# from array import *
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

print("Data is : ")
for i in range(a):
    rowsum = 0
    colsum = 0
    for j in range(b):
        print(arr[i][j],end=' ')
        rowsum = rowsum + arr[i][j]
        colsum = colsum + arr[j][i]
    print(" ->",i+1,"st Row sum is:",rowsum,end=" ")
    print(" ->",i+1,"st Col sum is:",colsum,end=" ")
    print('\n')



    




























