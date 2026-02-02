lst=[]
n=int(input("Enter number of elements:"))

for i in range(n):
    lst.append(int(input()))

lst=list(set(lst))
lst.sort()
print("Sorted list",lst)