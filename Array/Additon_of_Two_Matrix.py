# Addition of two Matrix 
arr1 = []
arr2 = []
sumArr = []

print("Enter the Dimesion of 2D matrix: ")
n = int(input())
m = int(input())


print("Enter the Data of first Matrix:  ")
for i in range(n):
    arr1.append([])
    for j in range (m):
        arr1[i].append(int(input()))

print("Enter the Data of Second Matrix:  ")
for i in range(n):
    arr2.append([])
    for j in range (m):
        arr2[i].append(int(input()))

# for doing operation in New Array i must have to Initialize by this method for doing operation .

sumArr = [[0 for j in range(m)] for i in range(n)] #initialization methond


print("First Matrix is: ")
for i in range(n):
    for j in range(m):
        print(arr1[i][j],end=' ')
    print()

print("Second Matrix is: ")
for i in range(n):
    for j in range(m):
        print(arr2[i][j],end=' ')
    print()

print("Addition of Matrix is: ")
for i in range(n):
    for j in range(m):
        sumArr[i][j] = arr1[i][j]+arr2[i][j]
        print(sumArr[i][j], end=' ')
    print()



    




























