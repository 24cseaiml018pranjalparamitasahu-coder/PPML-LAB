####################################ASSIGNMENT 4#################################################
#WAP TO PRINT SECOND LARGEST AND SECOND SMALLEST ELEMENT IN A LIST OF 10 INTEGERS WITHOUT USING SORT FUNCTIONS
arr=[]
x=int(input("Enter the no of elements:"))
for i in range(x):
    m=int(input("Enter the element: "))
    arr.append(m)
for j in range(len(arr)-1):
    for k in range (len(arr)-j-1):
        if arr[k]>arr[k+1]:
            arr[k],arr[k+1]=arr[k+1],arr[k]
print("The sorted array is:")
print(arr)
second_largest=arr[-2]
second_smallest=arr[1]
print("The second largest element is:",second_largest)
print("The second smallest element is:",second_smallest)