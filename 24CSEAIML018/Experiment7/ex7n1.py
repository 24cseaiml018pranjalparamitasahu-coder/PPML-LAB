m=int(input("Enter m:"))
n=int(input("Enter n:"))
lst=[]
for i in range(m,n+1):
    lst.append(i)
print("List:-",lst)
print("Sum:-",sum(lst))
print("Average:-",sum(lst)/len(lst))
print("Largest:-",max(lst))
print("Smallest:-",min(lst))
lst2=[]
for i in lst:
    if i%3 !=0:
        lst2.append(i)
print("List excluding multiples of 3: ",lst2)