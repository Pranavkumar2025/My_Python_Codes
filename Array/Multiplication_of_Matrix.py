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

print("Multiplication of Matrix is: ")
for i in range(n):
    for j in range(m):
        sum =0
        for k in range(n):
            prd = arr1[i][k] * arr2[k][j]
            sum = sum + prd
        sumArr[i][j] = sum
        print(sumArr[i][j],end=' ')    
    print()



    




























