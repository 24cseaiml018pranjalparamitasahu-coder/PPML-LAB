i=input("Enter a sentence:-")
list1=i.split()
print("\n Elements of the list1 with index:-")
for i,w in enumerate(list1):
    print(i,w)
list2=list(range( 1,len(list1)+1))
list3=list(zip(list1,list2))
print("\n combined list3 using zip")
print(list3)